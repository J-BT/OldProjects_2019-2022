

class Config:
    """
    Retrieves private informations such as database password or email account in the config.txt
    Inside the config.txt:
        -> A text preceded by # is ignored
        -> The config.txt must be filled as followed :
            DB_USER {your_DB_USER}
            DB_PASS {your_DB_PASS}
            IP {your_IP}
            DB_PORT {your_DB_PORT}
            DB_NAME {your_DB_NAME}

            outlook_account {your_outlook_account}
            outlook_password {outlook_password}

    """

    DB_USER: str = None
    DB_PASS: str = None
    IP: str = None
    DB_PORT: int = None
    DB_NAME: str = None
    outlook_account: str = None
    outlook_password: str = None

    @staticmethod
    def get_setting() -> dict:
        """
        Read the setting.txt file and retrieve informations such as the location 
        of your own config.txt file if exists. If it doesn't exist the method will 
        use the default config.txt located at the root of the folder
        """
        f = open("../setting.txt", "r")
        settings = f.readlines()
        f.close()

        all_settings = {}

        def trim_line(line: str) -> str:
            """
            Selects wanted informations in the config.txt removing spaces and variables
            """
            line = line.replace("\n", "").split(' ')[1]
            
            return line

        for setting in settings:
            if "#" not in setting:

                if ("config_location" in setting) :
                    all_settings["config_location"] = trim_line(setting)
                    
                    
        return all_settings    

        

    def get_infos(self):
        """
        Stores informations inside the config.txt in an instance of Config
        """
        settings =  Config.get_setting()

        try:
            f = open(f"{settings['config_location']}", "r")
            infos = f.readlines()
            f.close()
            print(f'Using {settings["config_location"]}')

        except:

            f = open(f"../config.txt", "r")
            infos = f.readlines()
            f.close()
            print(f'Using default config.txt')
        
        def trim_line(line: str) -> str:
            """
            Selects wanted informations in the config.txt removing spaces and variables
            """
            line = line.replace("\n", "").split(' ')[1]
            
            return line

        for info in infos:
            if "#" not in info:

                if ("DB_USER" in info) :
                    self.DB_USER = trim_line(info)
                    
                elif ("DB_PASS" in info) :
                    self.DB_PASS = trim_line(info)
                    
                elif ("IP" in info) :
                    self.IP = trim_line(info)
                    
                elif ("DB_PORT" in info) :
                    self.DB_PORT = trim_line(info)
                    
                elif ("DB_NAME" in info) :
                    self.DB_NAME = trim_line(info)
                    
                elif ("outlook_account" in info) :
                    self.outlook_account = trim_line(info)
                    
                elif ("outlook_password" in info) :
                    self.outlook_password = trim_line(info)
        return self

if __name__ == "__main__":
    pass