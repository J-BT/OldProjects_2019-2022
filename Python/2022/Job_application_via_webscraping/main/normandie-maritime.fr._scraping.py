import requests
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from sqlalchemy import or_

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
import smtplib
import os
import time

from config import Config


# Getting ids and others private informations stored in config.txt 
config = Config()
config.get_infos() 

# Connecting to the database
connection_string = f"postgresql://{config.DB_USER}:{config.DB_PASS}@{config.IP}:{config.DB_PORT}/{config.DB_NAME}"
engine = create_engine(connection_string)
Base = declarative_base() 

VERBOSE = False

class Company(Base):
    """
    Gathers informations about companies such as name, email or website.
    Its methods enable to save infos in a database as well as in an excel file.
    Moreover the send_email() static method can send a email to all the companies
    """
    def __init__(self,
                 name: str,
                 description: str,
                 website: str,
                 email: str,
                 address: str,
                 contactName: str) -> None:
        self.name = name
        self.description = description
        self.website = website
        self.email = email
        self.address = address
        self.contactName = contactName
        
    __tablename__ = "companies_www.normandie-maritime.fr"
    __table_args__ = {'extend_existing': False} 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    website = Column(String)
    email = Column(String)
    contactName = Column(String)
    email_sent = Column(Boolean, unique=False, default=False)

    def __repr__(self) -> str:
        return f"Company(id={self.id}, name={self.name}, email={self.email}, email_sent={self.email_sent})"
    
    def to_serie(self) -> pd.Series:
        """
        Convert an instance of Company into a pandas serie.
        Then several series can be merged in a pandas DataFrame
        """
        company = {
            'nom' : [self.name],
            'description' : [self.description],
            'site web' : [self.website],
            'email' : [self.email], 
            'adresse' : [self.address],
            'contact' : [self.contactName]
        }
        
        serie = pd.Series(company)
        return serie
    
    @staticmethod
    def retrieve_companies_pages() -> list[str]:
        """
        Get companies url from https://www.normandie-maritime.fr/annuaire-activites-maritimes.html
        and return them as a list
        """
        companies_links = []
        page = requests.get(f"https://www.normandie-maritime.fr/annuaire-activites-maritimes.html")
        soup = BeautifulSoup(page.content, 'html.parser')

        # On recupere l'url des pages d'informations des entreprises
        companies = soup.find_all("a", class_="infosOrganisme")
        
        for company in companies:
            #print(company['href'])
            companies_links.append(company['href'])
        
        return companies_links
    
    @staticmethod
    def create_table() -> None:
        #checkfirst – Defaults to True, don’t issue CREATEs for tables already present in the target database.
        status = Base.metadata.create_all(engine, checkfirst=True)
        print("Table companies created in database")
    
    @staticmethod
    def save(companies_links: list["Company"]) -> pd.DataFrame:
        try:
            """
            Save infos about companies in the database as well as in an excel file
            It takes a list of 'Company' objects as paramter and return a dataframe
            """

            list_of_series = []
            companies_list = []

            for companies_link in companies_links:
                information_page = requests.get(f"https://www.normandie-maritime.fr/{companies_link}")
                information_soup = BeautifulSoup(information_page.content, 'html.parser')

                #name
                name = information_soup.find("p",  class_="titre").text

                #description
                try:
                    #description = information_soup.find("p",  attrs={'style' : 'text-align: left;'}).text
                    description = information_soup.find("div",  class_ = "detailsTexte").text.replace("\n", "")

                except:
                    description = "NaN"

                #website
                try:
                    website = information_soup.find("a",  class_="detailsIcon url")['href']

                except:
                    website = "NaN"

                #email
                container = information_soup.find("p", class_="detailsIcon email")
                mailto = container.findChildren("a" , recursive=False)
                email = ""
                for element in mailto:
                    email = element['href'].replace("mailto:", "")
                    if email == "":
                        email = "NaN"

                #address
                address = information_soup.find("p",  class_="detailsIcon adresse").text

                #contactName
                contactName = information_soup.find("p",  class_="detailsIcon nomContact").text

                company = Company(name, description, website, email, address, contactName)
                companies_list.append(company)
                list_of_series.append(company.to_serie())

            # Saving in database : table companies 
            with Session(engine) as session: 
                for company in companies_list:

                    query = select(Company).filter(
                        or_(Company.name == company.name,
                            Company.email == company.email))

                    query_result = session.scalars(query).first()

                    if query_result is None:
                        session.add(company)
                        print(f"The following company has been added : {company.name} / {company.email}")

                    else:
                        print(f"*** {query_result.name} already in the database ***")
                session.commit()

            # All the series with companies' infos are gatheredin one dataframe
            all_companies = pd.DataFrame(list_of_series)
            # Which is stored in the following an excel file
            all_companies.to_excel("../companies/SocietesMaritimes.xlsx") 

            print("done")
            return all_companies
        
        except:
            print("Saving not possible")  
            return ""

    @staticmethod
    def get_all_companies() -> pd.DataFrame:
        print("Getting companies's information via web scraping...")
        try:
            # Getting url with companies infos
            companies_links = Company.retrieve_companies_pages()
            # Creating table : companies if doesn't exist
            Company.create_table()
            # Populating table & excel file
            all_companies = Company.save(companies_links)

            print("All companies are saved")
            
            return all_companies
        
        except:
            data = []
            df = pd.DataFrame(data)
            print("Something went wrong...")
            return data



    @staticmethod        
    def send_email_to_all():
        """
        Send an email to each company stored in the database if email_sent == False
        """
        start = time.time()
        email = Email()

        # Saving in database : table companies 
        with Session(engine) as session: 
            query = select(Company).filter(Company.email_sent == "FALSE") 
            query_results = session.execute(query)
            total_email_sent = 0
            # If companies saved in database haven't received an email yet 
            if query_results is not None:
                for company in query_results.scalars():
                    if company.email != "NaN" and company.name != "" and company.website != "NaN":

                        email.get_email_content(f"{company.name}")  # Stores email_content in email + replace send_to by company's name
                        email.send_email(f"{company.email}") 

                        session.query(Company).\
                            filter(Company.id == company.id).\
                            update({'email_sent': True})
                        total_email_sent += 1

                session.commit()
                print(f"Emails sent to all the companies - Total {total_email_sent}")

            else:
                print(f"*** No email has been sent ***")

        end = time.time()
        print(f"Execution time : {end - start}s")

    @staticmethod        
    def send_email_to_all_for_testing(adress_for_testing: str):
        """
        Takes an email adress as parameter and sends it n emails.
            n = number of companis stored in the database if email_sent == False
        """
        start = time.time()
        email = Email()

        # Saving in database : table companies 
        with Session(engine) as session: 
            query = select(Company).filter(Company.email_sent == "FALSE") 
            query_results = session.execute(query)
            total_email_sent = 0
            # If companies saved in database haven't received an email yet 
            if query_results is not None:
                for company in query_results.scalars():
                    if company.email != "NaN" and company.name != "" and company.website != "NaN":

                        email.get_email_content(f"{company.name}")  # Stores email_content in email + replace send_to by company's name
                        email.send_email(adress_for_testing) 

                        session.query(Company).\
                            filter(Company.id == company.id).\
                            update({'email_sent': True})
                        total_email_sent += 1

                session.commit()
                print(f"Emails sent to all the companies - Total {total_email_sent}")

            else:
                print(f"*** No email has been sent ***")

        end = time.time()
        print(f"Execution time : {end - start}s")

    @staticmethod        
    def send_email_for_testing(test_email_adress: str) -> str:
        """
        Send an email for testing 
        """
        start = time.time()
        email = Email()

        try:
       
            email.get_email_content(f"T.E.S.T Corp")  
            email.send_email(test_email_adress) 

            print(f"Test email OK")

        except:
            print(f"*** No email has been sent ***")

        end = time.time()
        print(f"Execution time : {end - start}s")  


    @staticmethod        
    def reset_email_sent():
        """
        Reset email_sent stats to False
        """
        start = time.time()
        email = Email()

        # Saving in database : table companies 
        with Session(engine) as session: 
            query = select(Company).filter(Company.email_sent == "TRUE") 
            query_results = session.execute(query)
            total_reset = 0

            # If companies saved in database haven't received an email yet 
            if query_results is not None:
                for company in query_results.scalars():
                    if company.email != "" and company.name != "":


                        session.query(Company).\
                            filter(Company.id == company.id).\
                            update({'email_sent': False})
                        total_reset += 1

                session.commit()
                print(f"Company's email_sent status reset - Total {total_reset}")

            else:
                print(f"*** No email_sent status has been reset ***")

        end = time.time()
        print(f"Execution time : {end - start}s")

class Email:
      
    subject: str = ""
    text: str = ""
    attachment: str = None
        
    def get_email_content(self, send_to: str):
        """
        Retrieves the content of email_content.txt and store it in an instance of Email
        """
        
        if(os.path.exists('../email/content/my_email_content.txt')):
            f = open("../email/content/my_email_content.txt", "r")
            lines = f.readlines()
            f.close()
        else:
            f = open("../email/content/email_content.txt", "r")
            lines = f.readlines()
            f.close()
        
    
        def format_line(line: str) -> str:
            """
            Replaces '\n' by '<br/>' in email_content.txt and send_to by company's name
            """
            line = line.replace("\n", "<br/>")
            if "send_to" in line:
                line = line.replace("send_to", send_to)

            return line
        
        def trim_line(line: str) -> str:
            """
            Selects wanted informations in the email_content.txt removing the '=' and variables
            """
            line = line.replace("\n", "").split('=')[1]
            
            return line
        
        
        for line in lines:
            if "#" in line:
                if ("subject=" in line) :
                    self.subject = trim_line(line)
                elif ("attachment=" in line) :
                    self.attachment = trim_line(line)
                    self.attachment = "../email/attachment/" + self.attachment
                    if self.attachment == "../email/attachment/":
                        self.attachment = None
            else:
                self.text += format_line(line)
            
        
        return self
    

    def send_email(self, mail_to: str) -> str:
        """
        Get the companies email adress stored in the database and send them and email if email_sent =false
        """
        start = time.time()

        try:

            # build message contents
            msg = MIMEMultipart()
            msg['Subject'] = self.subject  # add in the subject
            msg["To"] = mail_to
            msg["From"] = config.outlook_account
            msg.attach(MIMEText(self.text, "html"))  # add text contents
            
            if VERBOSE:
                print("OK avant piece jointe")
            # we do the same for attachments as we did for images
            if self.attachment is not None:
                if type(self.attachment) is not list:
                    attachment = [self.attachment]  # if it isn't a list, make it one

                for one_attachment in attachment:
                    with open(one_attachment, 'rb') as f:
                        # read in the attachment using MIMEApplication
                        file = MIMEApplication(
                            f.read(),
                            name=os.path.basename(one_attachment)
                        )
                    # here we edit the attached file metadata
                    file['Content-Disposition'] = f'attachment; filename="{os.path.basename(one_attachment)}"'
                    msg.attach(file)  # finally, add the attachment to our message object
            if VERBOSE:
                print("OK avant smtp")
             # initialize connection to our email server, we will use Outlook here
            smtp = smtplib.SMTP('smtp-mail.outlook.com', port='587')

            if VERBOSE:
                print("OK avant ehlo")
            smtp.ehlo()  # send the extended hello to our server

            if VERBOSE:
                print("OK avant starttls")
            smtp.starttls()  # tell server we want to communicate with TLS encryption

            if VERBOSE:
                print("OK avant login")
            smtp.login(config.outlook_account, config.outlook_password)  # login to our email server

            if VERBOSE:
                print("OK avant send_message")
            # send our email message 'msg' to our boss
            smtp.send_message(msg)

            if VERBOSE:
                print("OK avant close")
            smtp.close()  # finally, don't forget to close the connection

            end = time.time()

            return print(f"Candidature Envoyée à {mail_to} - time : {end - start}s")

        except:
            end = time.time()

            return print(f"L'envoi a renconté un problème - time : {end - start}s")
  

if __name__ == "__main__":
    ## Save companies in the database ###
    GET_COMPANIES = False

    ## (Test) emails ###
    RESET_EMAIL_SENT_STATUS = False
    SEND_ONE_EMAIL_FOR_TESTING = False
    SEND_EMAIL_TO_ALL_COMPANIES_FOR_TESTING = False

    ## Emails ###
    SEND_EMAIL_TO_ALL_COMPANIES = False

    ## Settings ###
    PRINT_SETTINGS = False

    if GET_COMPANIES:
        Company.get_all_companies()

    if SEND_ONE_EMAIL_FOR_TESTING:
        Company.send_email_for_testing("your_adress_for_testing@goes_here.com")
    if SEND_EMAIL_TO_ALL_COMPANIES_FOR_TESTING:
        Company.send_email_to_all_for_testing("your_adress_for_testing@goes_here.com")
    if SEND_EMAIL_TO_ALL_COMPANIES:
        Company.send_email_to_all()
    if RESET_EMAIL_SENT_STATUS:
        Company.reset_email_sent()
        
    if PRINT_SETTINGS:
        print(Config.get_setting())