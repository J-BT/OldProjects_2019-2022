#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from datetime import (datetime, timedelta)
import random

# Pour tests ajouts transferts sur 1 an -------------------------------------
import sys
sys.path.append('..') #Permet d'acceder aux dossiers parents
from app_stocks_info_hpe.__init__ import (engine, app, db)
from app_stocks_info_hpe.models import (Service, Materiel,
                                        Transfert, Materiel_destocke)
# Pour realiser des Sessions sur bdd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func #Permet d'appeler la foncion count


"""
Afin de tester l'application de gestion de base de donnéees du service info
de l'HPE', nous allons générer automatiquement des données aléatoire
pour peupler la base de données
"""

materiel_info=[('Souris'),
               ('Clavier'),
               ('Serveur'),
               ('PC Portable'),
               ('Station de travail'),
               ('PC de bureau'),
               ('Accessoire PC de bureau'),
               ('Téléphone'),
               ('Tablette'),
               ('Sacoche PC'),
               ('Chargeur PC portable'),
               ('Batterie externe PC portable'),
               ('Processeur'),
               ('Refroidissement'),
               ('Mémoire RAM'),
               ('HDD'),
               ('SSD'),
               ('Carte mère'),
               ('Carte graphique'),
               ('Boîtier PC'),
               ('Alimentation PC'),
               ('Graveur DVD'),
               ('Graveur BLURAY'),
               ('Carte Son'),
               ('Carte Contrôleur'),
               ('Moniteur LCD'),
               ('Imprimante'),
               ('Onduleur'),
               ('Enceinte'),
               ('Casque'),
               ('Microphone'),
               ('Webcam'),
               ('Réseau'),
               ('Switch'),
               ('Modem'),
               ('Routeur'),
               ('Réseau WiFi'),
               ('Câble RJ45'),
               ('Câble fibre optique'),
               ('Vidéo surveillance'),
               ('Caméra IP'),
               ('Enregistreur NVRDVR'),
               ('Câble USB'),
               ('Adaptateur USB'),
               ('Câble VIDEO'),
               ('Adaptateur VIDEO'),    
               ('Câble AUDIO'),
               ('Adaptateur AUDIO'),
               ('Câble SECTEUR'),
               ('Adaptateur SECTEUR'),
               ('Câble TELEPHONIE'),
               ('Adaptateur TELEPHONIE')
               ]

# Pour communiquer avec bdd
Session = sessionmaker(bind=engine)
session = Session()

def retrait_materiel(ligne_materiel, qte_materiel):
    """
    *********************************************
    **Fonction Appelée par generation_tranferts**
    *********************************************
    Lorsqu'un transfert est effectué, on appelle cette fontion pour deduire 
    la quantité de matériel transferée du stock disponible
    """
    session.query(Materiel).filter(
        Materiel.id_materiel==ligne_materiel).update(
            {Materiel.qte_materiel: qte_materiel})
    session.commit()

def ajout_mat_destoke(mat,des,qte,cout,rais):
    """
    *********************************************
    **Fonction Appelée par generation_tranferts**
    *********************************************
    On va egalement peupler la table "Materiel_destocke" pour chaque transfert
    effectué à l'aide de cette fonction
    """
    ajout = Materiel_destocke(nom_mat_destocke=mat,
                              destination_destockage=des,
                              quantite_destockage=qte,
                              cout_destockage=cout,
                              raison_destockage=rais)
    session.add(ajout)
    session.commit()

def restockage_materiel(qte_commandee):
    """
    *********************************************
    **Fonction Appelée par generation_tranferts**
    *********************************************
    Quand un element de la table Materiel aura une qté <= 4
    cette fonction ajoutera automatiquement des qté au produit,
    ainsi le stock dispo pr ce materiel sera == 20
    
    """
    session.query(Materiel).filter(
        Materiel.qte_materiel <= 4).update(
            {Materiel.qte_materiel: qte_commandee})
    session.commit()
    
materiel_a_cder = session.query(Materiel).filter(
            Materiel.qte_materiel <= 4)
    

def generation_de_stocks():
    """
    On peuple la table Materiel grâce à la liste materiel_info.
    on affectera pour chaque element de la liste un stock compris entre
    40 et 60
    """
    np.random.seed(0) #<---quand == 0, ne reset pas donnéees aléatoires
    ligne_pour_bdd = []
    materiel_a_inserer = {}
    id_provisoire = 0
    
    for materiel in materiel_info:
        ligne_pour_bdd = []
        prod_name = materiel
        prod_qty = float(np.random.randint(
           40, 60, 1)) 
        gamme_prix = [9.5, 19.75, 279.99, 350, 555.02, 999.99, 37555.90]
        poids_prix = [0.2, 0.4, 0.1, 0.05, 0.05, 0.19, 0.01]
        prod_prix = float(np.random.choice(gamme_prix, p=poids_prix)) 
        ligne_pour_bdd.append(prod_name)
        ligne_pour_bdd.append(prod_qty)
        ligne_pour_bdd.append(prod_prix)
        materiel_a_inserer[id_provisoire] = ligne_pour_bdd
        id_provisoire += 1
    
    return pd.DataFrame.from_dict(materiel_a_inserer, orient='index')


def generation_tranferts():
    """
    On génere des transferts sur une periode comprise entre [date_debut]
    et [date_fin]
    Pour chaque jour de la perode choisie:
        1) On selectionne un service au hazard
        2) On tire au hazard un matériel informatique
                
        3) Puis on transfere un qté du matériel comprise entre [0 & 3]
                au service tiré au sort
        
        ** Parallèlement aux transferts :
            - on déduira la qté transférée au service
            du stock disponible (Table = Materiel)
            - on peuplera egalement la table Materiel_destocke en plus de 
            la table Transfert
            - on ajoutera du stock disponible quand les qté dispo d'un 
            produit sera <= 4
    """
    date_debut = datetime(2020, 1, 1)
    date_fin = datetime(2021, 1, 1) 
    mat_dispo_trans = 0 # a effacer
    #np.random.seed(1) # Si l'on veut un random qui ne change qu'une fois
    transferts_annee = {}
    id_produit = 0
    dates = pd.date_range(date_debut,
                          date_fin - timedelta(days=1),
                          freq = 'd')
    
    for date in dates:
        ligne = []
        #####################################################################
        #################### Service origine ################################
        #####################################################################
        service_origne = ('Stocks Informatique')
        
        ######################################################################
        #################### Transferer à quel service #######################
        ######################################################################
        # on check les services dispo
        serv_dispo_trans = Service.query.with_entities(
            Service.id_service,
            Service.nom_service).all()
        # on les compte
        nombre_serv_dispo = Service.query.count()
        # on tire au sort ligne entre [1 et nb_services]
        ligne_au_hazard_s = int(
            np.random.randint(1, nombre_serv_dispo + 1, 1))
        # on selectionne le service correspondant à la ligne tirée au hazard
        service_transfere = Service.query.filter_by(
            id_service=ligne_au_hazard_s).first()
        #____________________________________________________________________#
        
        ######################################################################
        #################### Quel matériel transferer ########################
        ######################################################################
        mat_dispo_trans = Materiel.query.with_entities(
            Materiel.id_materiel,
            Materiel.nom_materiel,
            Materiel.qte_materiel,
            Materiel.prix_unitaire).all()
        #on compte le nombre d'element dans Materiel pour limiter 
        # la f(x) range
        nombre_mat_dispo = Materiel.query.count()
        # on tire au sort un nombre au hazarde entre 1 et 
        # nombre de type de mat dispo
        ligne_au_hazard_m = int(np.random.randint(1, nombre_mat_dispo + 1, 1))
        materiel_a_transferer = Materiel.query.filter_by(
                id_materiel=ligne_au_hazard_m).first()
        
        # On stocke dans qte_reelle la qté de mat disponible
        qte_reelle = int(Materiel.query.filter_by(
            id_materiel=ligne_au_hazard_m).first().qte_materiel)
        qte_hazard = int(np.random.randint(1, 4, 1))
        if qte_reelle > 0:
        ######################################################################
        #################### Quelle quantité transferer ######################
        ######################################################################
            # Afin que l'on puisse retirer qté <= au stock réel
            while qte_hazard > qte_reelle:
                qte_hazard = int(np.random.randint(1, 4, 1))
            
        #____________________________________________________________________#
        else: 
            pass
            #print("C'est inférieur à zero ")
        
        #####################################################################
        #################### Pour quelle raison #############################
        #####################################################################
        raisons = ['Casse', 'Vol', 'Defectueux', 'Mise a niveau']
        poids_raison = [0.25, 0.05, 0.5, 0.2]
        raison_transf = np.random.choice(raisons, p=poids_raison)
        
        # gamme_prix = [9.5, 19.75, 279.99, 350, 555.02, 999.99, 37555.90]
        # poids_prix = [0.2, 0.4, 0.1, 0.05, 0.05, 0.19, 0.01]
        # prod_prix = float(np.random.choice(gamme_prix, p=poids_prix)) 
        #____________________________________________________________________#

        #####################################################################
        ####     On retire qté transférée du Matériel correspondant     #####
        #####################################################################
        

        # On retire la qté de materiel correspondante
        retrait_materiel(ligne_au_hazard_m, qte_hazard)
        
        # S'il y a moins de 8 unité de materiel, on remet stock à 20
        materiel_a_cder = session.query(Materiel).filter(
            Materiel.qte_materiel <= 4)
        
        if str(materiel_a_cder) != 'None':
            restockage_materiel(20)

        cout_tranf = (qte_hazard * materiel_a_transferer.prix_unitaire)
        
        ajout_mat_destoke(materiel_a_transferer.nom_materiel,
                          service_transfere.nom_service,
                          qte_hazard,
                          cout_tranf,
                          raison_transf)
        
        ajout_valeur_stock()

     
        ligne.append(date)
        ligne.append(service_origne)
        ligne.append(service_transfere.nom_service)
        ligne.append(materiel_a_transferer.nom_materiel)
        ligne.append(qte_hazard)
        ligne.append(cout_tranf)
        ligne.append(raison_transf)
        transferts_annee[id_produit] = ligne
        
        
        
        id_produit += 1
    return pd.DataFrame.from_dict(transferts_annee, orient='index')

def recup_noms_service():
    """
    Retourne une liste contenant le nom des services
    enregistrés dans la bdd
    """
    les_services = []
    noms_services = Service.query.all()
    ligne = 0
    for service in noms_services:
        # print(noms_services[ligne].nom_service)
        serv = noms_services[ligne].nom_service
        les_services.append(serv)
        ligne +=1
    return les_services


    
def recup_nb_occurences_services():
    """
    On compte le nombre de fois qu'un service s'est fait transférer
    du matériel sur toute la periode.
    Les resultats serviront à alimenter le Bar_chart du dashboard admin
    *****
    **NB**
    *****
    ( en divisant par le nombre total de transfert on peut egalment
     deduire le pourcentage de transfert/ service)
    """

    nb_occurences_services = session.query(Transfert.destination_transfert,
                  func.count(Transfert.destination_transfert)).group_by(
                      Transfert.destination_transfert).all()
    
    occurence_par_service = {}
    ligne = 0
    for occurence in nb_occurences_services:
        # on transforme en liste pour acceder aux elements
        element_pour_dico = list(nb_occurences_services[ligne])
        # On affecte le 1er element en clé dico et 2eme en valeur
        occurence_par_service[element_pour_dico[0]] = element_pour_dico[1]
        ligne += 1
    
    return occurence_par_service

def recup_cout_par_service():
    """
    On va compter va additionner les coûts de chaque service pour
    les reprsenter graphiquement 
    """
    df = pd.read_sql_table('transfert', engine)
    infos_bar_chart = df[["destination_transfert", "cout_transfert"]]
    cout_par_service = infos_bar_chart.groupby(["destination_transfert"]).sum()
    cout_par_service.sort_values(by=["cout_transfert"],
                                 inplace=True,
                                 ascending=False)
    couts =  cout_par_service.to_dict()
    #dict.keys() and dict.items()
    couts_par_service = couts['cout_transfert']
    
    
    return couts_par_service
    
    
   
def recup_pourcent_raisons_transf():
    """
    Grâce à une query de SQLALchemy, on va compter le nombre d'occurences
    pour chaque raison de transfert, puis on divisera ces dernieres par
    le nombre total de transfert sur toute la periode.
    Ainsi, on determinera le pourcentage de chaque raison sur toute la periode 
    de transferts     
    """
    nb_occurences_raisons = session.query(Transfert.raison_transfert,
                      func.count(Transfert.raison_transfert)).group_by(
                          Transfert.raison_transfert).all()
    
    total_transferts = Transfert.query.count()
    occurence_raisons = {}
    ligne = 0
    
    for occurence in nb_occurences_raisons:
        elem_dico = list(nb_occurences_raisons[ligne])
        poucentage_rais = elem_dico[1]/total_transferts
        occurence_raisons[elem_dico[0]] = round(poucentage_rais, 2)
        ligne += 1
   
    return occurence_raisons

def millisec_en_datetime(ms):
    """
    On transforme le format d'une date  :
        de milliseconde à datetime  
    """
    date = datetime.datetime.fromtimestamp((ms/1000.0))
    return date

def datetime_to_ms(dt_obj):
    """
    On transforme le format d'une date  :
        de datetime à milliseconde  
    """
    millisec = dt_obj.timestamp() * 1000
    return millisec


def ajout_valeur_stock():
    """
    Dans la colonne [valeur_stock] de la table Materiel:
    On va ajouter le produit (Materiel.qte_materiel * Materiel.prix_unitaire)
    """
    
    #on calcule le produit de (qté de matériel * prix unitaire)
    val_stock_ligne = Materiel.qte_materiel * Materiel.prix_unitaire
    nb_mat_total = Materiel.query.count()
    # Pour chaque ligne de la table Materiel
    for ligne in range(1, nb_mat_total + 1):
        session.query(Materiel).filter(
                Materiel.id_materiel == ligne).update(
                    {Materiel.valeur_stock: val_stock_ligne})
    session.commit()


### TESTS


EFFACER_BDD = False

PEUPLER_MATERIEL = False

PEUPLER_TRANSFERT = False

TEST_QUERY_BDD = False

TEST_QUERY_NOMBRE_OCCURENCE_SERV = True

TEST_QUERY_NOMBRE_OCCURENCE_RAISONS = False



if __name__ == '__main__':
    if EFFACER_BDD:      
        Materiel.__table__.drop(engine)
        Service.__table__.drop(engine)
        Transfert.__table__.drop(engine)
        Materiel_destocke.__table__.drop(engine)
                
    
    elif PEUPLER_MATERIEL:
        df = generation_de_stocks()
        df.columns = ['nom_materiel','qte_materiel','prix_unitaire']
        print(df)

    
    elif PEUPLER_TRANSFERT:
            colonnes = ["horodatage_transfert",
                "origine_transfert",
                "destination_transfert",
                "nom_produit_transfert",
                "quantite_transfert",
                "cout_transfert",
                "raison_transfert"]
            transferts_a_inserer = generation_tranferts()
            #on y ajoute des noms de colonnes
            transferts_a_inserer.columns = colonnes
            # print(transferts_a_inserer)
            # puis on transforme le tout en table sql & l'insere ds : "materiel" 
       
            transferts_a_inserer.to_sql(
                'transfert',
                con=db.engine,
                if_exists='append',
                index=False)

    
    elif TEST_QUERY_BDD:
        les_services = recup_noms_service()
        for service in les_services:
            print(service)
    
    
    elif TEST_QUERY_NOMBRE_OCCURENCE_SERV:
        occurences_par_service = recup_nb_occurences_services()
        # for ligne in occurences_par_service:
        #     print(ligne)
        print(occurences_par_service)
        # print(type(occurences_par_service))

    elif TEST_QUERY_NOMBRE_OCCURENCE_RAISONS:
        occurence_raisons_pr_100 = recup_pourcent_raisons_transf()
        # for ligne in occurence_raisons_pr_100.values():
        #     print(ligne)
        print(occurence_raisons_pr_100)
