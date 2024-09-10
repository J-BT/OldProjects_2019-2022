#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TO_DO = 

4) implémenter ttes le foncitonnalités de highchart
"""
### Import bibliothèques -----------------------------------------------------
import numpy as np
import pandas as pd
from flask import (render_template, url_for, redirect,
                   flash, request, jsonify, make_response)
from datetime import (datetime, timedelta)
import random
from random import sample # <----- Pour tests sur graphiques js 
import time, datetime
from sqlalchemy.exc import IntegrityError
import requests
import json
# Pour realiser des Sessions sur bdd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func #Permet d'appeler la foncion count

### imports modules locaux ---------------------------------------------------
from app_stocks_info_hpe import app, db
from app_stocks_info_hpe.forms import (Ajoutermateriel, Modifiermateriel,
                                       Ajouterservice, Modifierservice,
                                       Transferermateriel)
from app_stocks_info_hpe.models import (Service, Materiel,
                                        Transfert, Materiel_destocke)
from app_stocks_info_hpe.donnees_reelles_pr_bdd import (
    services, raisons_transfert, generation_de_services)
from app_stocks_info_hpe.donnees_aleatoires_pr_bdd import (
    generation_de_stocks, generation_tranferts, recup_noms_service,
    recup_nb_occurences_services, recup_pourcent_raisons_transf,
    millisec_en_datetime, ajout_valeur_stock, recup_cout_par_service,
    datetime_to_ms)
from app_stocks_info_hpe.__init__ import engine


# Pour communiquer avec bdd
Session = sessionmaker(bind=engine)
session = Session()

### Variables globales -------------------------------------------------------

# Pour peupler :
# rafraichier page depuis Accueil ou Accueil_admin, puis
# aller à l'url Matériel puis de Service   
PEUPLER_TABLE_STOCKS_AVEC_LISTE = False   # en 1er
PEUPLER_TABLE_SERVICES_AVEC_LISTE = False # en 2eme
PEUPLER_TABLE_TRANSFERTS = False # en 3eme


# Page d'accueil--------------------------------------------------------------
@app.route("/", methods= ['GET','POST'] )
@app.route("/Accueil", methods= ['GET','POST'] )
def accueil():
    return render_template('accueil.html',
                           title = 'Accueil')


# Page d'accueil admin--------------------------------------------------------
@app.route("/Accueil_admin", methods= ['GET', 'POST'] )
def accueil_admin():
    #Execute la fonction pour recup le noms des services
    #en Jinja dans la page accueil_admin
    occurences_par_service = recup_nb_occurences_services()
    occurence_raisons_pr_100 = recup_pourcent_raisons_transf()
    services_pr_labels = []
    raisons_pr_labels = []
    # On recup les labels js    
    for serv in occurences_par_service:
        services_pr_labels.append(serv)
    
    # On recup les labels js    
    for rais in occurence_raisons_pr_100:
        raisons_pr_labels.append(rais)
    
    couts_par_service = recup_cout_par_service()
    
    return render_template('accueil_admin.html',
                           title = 'Accueil Administrateur',
                           services_pr_labels = services_pr_labels,
                           raisons_pr_labels = raisons_pr_labels,
                           couts_par_service=couts_par_service)


# Pour générer line chart dynamiquement
@app.route('/Highcharts', methods=["GET", "POST"])
def highcharts():
    payload = {}
    headers = {}
    url = "https://demo-live-data.highcharts.com/aapl-ohlcv.json"
    r = requests.get(url, headers=headers, data ={})
    r = r.json()
    j = []
    donnees_highchart = []
    donnees_highchart2 = []
    donnees_highchart3 = []
    donnees_highchart4 = []
    donnees_highchart5 = []
    donnees_highchart6 = []
    donnees_highchart7 = []
    donnees_highchart8 = []
    donnees_highchart9 = []
    donnees_highchart10 = []
    donnees_highchart11 = []
    donnees_highchart12 = []
    donnees_highchart13 = []
    ##################################################
    ### On change format date : de ms --> datetime ###
    ##################################################
        
    for col0, col1, col2, col3, col4, col5 in r:
        # Date - Prix - Volume #
        donnees_highchart.append([col0, col1])
        donnees_highchart2.append([col0, col1 + 12.5 ])
        donnees_highchart3.append([col0, col1 + 22.5 ])
        donnees_highchart4.append([col0, col1 + 32.5 ])
        donnees_highchart5.append([col0, col1 + 42.5 ])
        donnees_highchart6.append([col0, col1 + 52.5 ])
        donnees_highchart7.append([col0, col1 + 62.5 ])
        donnees_highchart8.append([col0, col1 + 72.5 ])
        donnees_highchart9.append([col0, col1 + 82.5 ])
        donnees_highchart10.append([col0, col1 + 92.5 ])
        donnees_highchart11.append([col0, col1 + 102.5 ])
        donnees_highchart12.append([col0, col1 + 112.5 ])
        donnees_highchart13.append([col0, col1 + 122.5 ])

    
            
    return {"res":donnees_highchart,
            "res2":donnees_highchart2,
            "res3":donnees_highchart3,
            "res4":donnees_highchart4,
            "res5":donnees_highchart5,
            "res6":donnees_highchart6,
            "res7":donnees_highchart7,
            "res8":donnees_highchart8,
            "res9":donnees_highchart9,
            "res10":donnees_highchart10,
            "res11":donnees_highchart11,
            "res12":donnees_highchart12,
            "res13":donnees_highchart13}

# Pour générer barchart dynamiquement
@app.route("/Bar_chart")
def bar_chart():
    couts_par_service = recup_cout_par_service()
    valeurs_Barchart = []
    for ligne in couts_par_service.values():
        valeurs_Barchart.append(ligne)
        
    return jsonify({'resultat' : valeurs_Barchart
                    })

# Pour générer barchart dynamiquement
@app.route("/Pie_chart")
def pie_chart():
    occurence_raisons_pr_100 = recup_pourcent_raisons_transf()
    valeurs_piechart = []
    
    for ligne in occurence_raisons_pr_100.values():
        valeurs_piechart.append(ligne)

    return jsonify({'defectueux' : valeurs_piechart[0],
                    'mise_a_niveau' : valeurs_piechart[1],
                    'casse' : valeurs_piechart[2],
                    'vol' : valeurs_piechart[3]
                    })

# Services -----------------------------------------------------------------
@app.route("/Service", methods = ['GET', 'POST'])
def service():
    ajouter_service = Ajouterservice()
    modifier_service = Modifierservice()
    tous_les_services = Service.query.all()
    est_ce_que_service = bool(Service.query.all())
    #________________________________________________________________#
    #### Si aucun service enregistré ################################# 
    if est_ce_que_service == False and request.method == 'GET':     
        if PEUPLER_TABLE_STOCKS_AVEC_LISTE:
            #generation_de_services() renvoit une DF
            services_a_inserer = generation_de_services()
            #on y ajoute le nom de la colonne
            services_a_inserer.columns = ['nom_service']
            #puis on transforme le tout en table sql & l'insere ds : "service"
            services_a_inserer.to_sql(
                'service',
                con=db.engine,
                if_exists='append',
                index=False)
            flash(' Les services ont été ajoutés','info')
            return redirect('/Service')
        else:
            flash('Ajoutez des services pour les visualiser','info')
    #________________________________________________________________#
    #### Si modification d'un service ################################
    if modifier_service.validate_on_submit() and request.method == 'POST':
        id_service_modifie_utilisateur = request.form.get(
            "idServiceModifie","")
        nom_service_modifie_utilisateur = request.form.get(
            "nomServiceModifie","")
        tous_les_services = Service.query.all()
        
        # On lie le service choisi par l'utilisateur au service correspondant
        # de la table Service:
        # id_service(bdd) = id_service_modifie(choix utilisateur)
        le_service_a_modif = Service.query.filter_by(
            id_service = id_service_modifie_utilisateur).first()
        # Puis on replace l'ancien nom de service par le nouveau
        # choisi par l'utilisateur
        le_service_a_modif.nom_service = modifier_service.modifnomservice.data
        
        # Puis on met à jour les tables : materiel_destocke & transfert
        Materiel_destocke.query.filter_by(
            destination_destockage=nom_service_modifie_utilisateur).update(
            dict(destination_destockage=modifier_service.modifnomservice.data))         
        Transfert.query.filter_by(
            origine_transfert=nom_service_modifie_utilisateur).update(
                dict(origine_transfert=modifier_service.modifnomservice.data))
        Transfert.query.filter_by(
            destination_transfert=nom_service_modifie_utilisateur).update(
            dict(destination_transfert=modifier_service.modifnomservice.data))
        try:
            db.session.commit()
            flash('Le service a été mis à jour!', 'success')
            return redirect(url_for('service'))
        except IntegrityError :
            db.session.rollback()
            flash('Ce service éxiste déjà','danger')
            return redirect('/Service')
    #________________________________________________________________#
    #### Si ajout d'un service #######################################
    elif ajouter_service.validate_on_submit() :
        le_service_a_modif = Service(
            nom_service=ajouter_service.nomservice.data)
        db.session.add(le_service_a_modif)
        try:
            db.session.commit()
            flash('Le Service {ajouter_service.nomservice.data} a été ajouté!',
                  'success')
            return redirect(url_for('service'))
        except IntegrityError :
            db.session.rollback()
            flash('Ce service existe déjà','danger')
            return redirect('/Service')
    return render_template('service.html',
                           title = 'Services',
                           modifier_service = modifier_service,
                           ajouter_service = ajouter_service,
                           tous_les_services=tous_les_services)

# Materiel -----------------------------------------------------------------
@app.route("/Materiel", methods = ['GET','POST'])
def materiel():
    ajouter_materiel = Ajoutermateriel()
    modifier_materiel = Modifiermateriel()
    tout_le_materiel = Materiel.query.all()
    est_ce_que_materiel = bool(Materiel.query.all())
    #______________________________________________________________#
    #### Si aucun stock de matériel ################################# 
    if est_ce_que_materiel== False and request.method == 'GET':
        if PEUPLER_TABLE_STOCKS_AVEC_LISTE:
            #generation_de_stocks() renvoit une DF
            stocks_a_inserer = generation_de_stocks()
            #on y ajoute des noms de colonnes
            stocks_a_inserer.columns = ['nom_materiel',
                                        'qte_materiel','prix_unitaire']
            #puis on transforme le tout en table sql & l'insere ds : "materiel"
            stocks_a_inserer.to_sql(
                'materiel',
                con=db.engine,
                if_exists='append',
                index=False)
            # on peuple la colonne valeur stock
            ajout_valeur_stock()
### Appel de la fonction [ajout_valeur_stock]
            flash(' Votre matériel a été crée ajouté','info')
            return redirect('/Materiel')
        else:
            flash('Ajoutez du matériel pour le visualiser','info')   

    #________________________________________________________________#
    #### Si modification d'un matériel ###############################
    if modifier_materiel.validate_on_submit() and request.method == 'POST':
        id_materiel_modifie_utilisateur = request.form.get(
            "idMaterielModifie","")
        nom_materiel_modifie_utilisateur = request.form.get(
            "nomMaterielModifie","")
        qte_materiel_modifie_utilisateur = request.form.get(
            "qteMaterielModifie","")
        prix_materiel_modifie_utilisateur = request.form.get(
            "prixMaterielModifie","")
        tout_le_materiel = Materiel.query.all()
        
        # On lie le materiel choisi par l'utilisateur au materiel correspondant
        # de la table Materiel:
        # id_materiel(bdd) = id_materiel_modifie(choix utilisateur)
        le_materiel_a_modif = Materiel.query.filter_by(
            id_materiel = id_materiel_modifie_utilisateur).first()
        # Puis on replace l'ancien nom du materiel par le nouveau
        # choisi par l'utilisateur
        le_materiel_a_modif.nom_materiel = modifier_materiel.modifnommateriel.data
        le_materiel_a_modif.qte_materiel = modifier_materiel.modifquantitemateriel.data
        le_materiel_a_modif.prix_unitaire = modifier_materiel.modifprixmateriel.data
        # On rempli egalement la colonne valeur_stock grace aux qte et p.u
        v_sto = modifier_materiel.modifprixmateriel.data * modifier_materiel.modifquantitemateriel.data
        le_materiel_a_modif.valeur_stock=(v_sto)
        # Puis on met à jour les tables : materiel_destocke & transfert
        Materiel_destocke.query.filter_by(
            destination_destockage=nom_materiel_modifie_utilisateur).update(
            dict(destination_destockage=modifier_materiel.modifnommateriel.data))         
        Transfert.query.filter_by(
            origine_transfert=nom_materiel_modifie_utilisateur).update(
                dict(origine_transfert=modifier_materiel.modifnommateriel.data))
        Transfert.query.filter_by(
            destination_transfert=nom_materiel_modifie_utilisateur).update(
            dict(destination_transfert=modifier_materiel.modifnommateriel.data))
        try:
            db.session.commit()
            flash('Le materiel a été mis à jour!', 'success')
            return redirect(url_for('materiel'))
        except IntegrityError :
            db.session.rollback()
            flash('Ce service éxiste déjà','danger')
            return redirect('/Materiel')
        return render_template('materiel.html',
                               title = 'materiaux',
                               tout_le_materiel=tout_le_materiel,
                               modifier_materiel=modifier_materiel)

    #______________________________________________________________#
    #### Si ajout d'un materiel ####################################
    elif ajouter_materiel.validate_on_submit() :
        le_materiel_a_ajouter = Materiel(
            nom_materiel=ajouter_materiel.nommateriel.data,
            qte_materiel=ajouter_materiel.quantitemateriel.data,
            prix_unitaire=ajouter_materiel.prixmateriel.data)
        db.session.add(le_materiel_a_ajouter)
        try:
            db.session.commit()
            # on peuple la colonne valeur stock
            ajout_valeur_stock()
            flash('Le Materiel {ajouter_materiel.nommateriel.data} a été ajouté!',
                  'success')
            return redirect(url_for('materiel'))
        except IntegrityError :
            db.session.rollback()
            flash('Ce materiel existe déjà','danger')
            return redirect('/Materiel')
    return render_template('materiel.html',
                           title = 'Materiel',
                           modifier_materiel=modifier_materiel,
                           ajouter_materiel = ajouter_materiel,
                           tout_le_materiel=tout_le_materiel)


# Delete -----------------------------------------------------------------
@app.route("/Delete")
def delete():
    """
    Quand utilisateur efface:
        - Du materiel:
            On enleve ligne choisie dans Materiel
        - Un service:
            On enleve ligne choisie dans Service
        - Un transfert:
            1) On enleve ligne choisie dans Transfert
            2) On enleve ligne corespondante dans Materiel_destocke
            3) On re-ajoute les qté transférées dans Materiel
            4) On re-ajoute les qté transférées le cout_transfert
                    dans colonne valeur_stock de Materiel
                    
    """
    choix_a_effacer = request.args.get('choix_effacement')
    if choix_a_effacer == 'materiel':
        ligne_mat_a_effacer = request.args.get(
            'id_materiel_modifie_utilisateur')
        materiel_a_effacer = Materiel.query.filter_by(
            id_materiel=ligne_mat_a_effacer).delete()
        db.session.commit()
        flash('Votre matériel a bien été effacé!', 'success')
        return redirect(url_for('materiel'))
        return render_template('materiel.html',title = 'Materiel')
    
    elif choix_a_effacer == 'service':
        ligne_serv_a_effacer = request.args.get(
            'id_service_modifie_utilisateur')
        service_a_effacer = Service.query.filter_by(
            id_service=ligne_serv_a_effacer).delete()
        db.session.commit()
        flash(f'Le service a bien été effacé!', 'success')
        return redirect(url_for('service'))
        return render_template('service.html',title = 'Services')
    
    elif choix_a_effacer == 'transfert':
        ligne_trans_a_effacer = request.args.get(
            'id_transf_modifie_utilisateur')
        # Effacement ligne Transfert
        trans_a_effacer = Transfert.query.filter_by(
            id_transfert=ligne_trans_a_effacer).delete()
        # Effacement ligne Materiel_destocke
        destock_a_eff = Materiel_destocke.query.filter_by(
            id_mat_destocke=ligne_trans_a_effacer).delete()
        
        # Ajout qté transferée dans Materiel
        bne_ligne = Transfert.id_transfert == ligne_trans_a_effacer
        qte_tranf = session.query(
            Transfert).filter(bne_ligne).first().quantite_transfert
        mat_concernee = session.query(
            Transfert).filter(bne_ligne).first().nom_produit_transfert
        bn_l_mat = Materiel.nom_materiel == mat_concernee
        mat_a_peupler = session.query(
            Materiel).filter(bn_l_mat).update(
                    {Materiel.qte_materiel: Materiel.qte_materiel + qte_tranf})
       
        # Ajout coût du transfert dans Materiel
        bne_ligne = Transfert.id_transfert == ligne_trans_a_effacer
        ct_tranf = session.query(
            Transfert).filter(bne_ligne).first().cout_transfert
        mat_concernee = session.query(
            Transfert).filter(bne_ligne).first().nom_produit_transfert
        bn_l_mat = Materiel.nom_materiel == mat_concernee
        val_a_peupler = session.query(
            Materiel).filter(bn_l_mat).update(
                    {Materiel.valeur_stock: Materiel.valeur_stock + ct_tranf})
        
        session.commit()
        
### Remettre le stock de matériel dans Matériel
        
        db.session.commit()
        flash(f'Le Transfert a bien été effacé!', 'success')
        return redirect(url_for('transfert'))
        return render_template('transfert.html',title = 'Transferts')

# Transfert  -----------------------------------------------------------------
@app.route("/Transfert", methods = ['GET', 'POST'])
def transfert():
    transferer_materiel = Transferermateriel()
    tous_les_transferts = Transfert.query.all()
    tout_le_materiel_trans = Materiel.query.all()
    est_ce_que_transfert = bool(Transfert.query.all())
    ##################################################################
    ####  Si aucun transfert enregistré ##############################
    ##################################################################
    if est_ce_que_transfert == False and request.method == 'GET' :
        if PEUPLER_TABLE_TRANSFERTS:
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
            #puis on transforme le tout en table sql & l'insere ds : "materiel"
            transferts_a_inserer.to_sql(
                'transfert',
                con=db.engine,
                if_exists='append',
                index=False)
            flash(' Votre Tranfert a été crée ajouté','info')
            return redirect('/Transfert')
        else:
            flash('Veuillez effectuer des transferts pour les visualiser',
                  'info')
    #________________________________________________________________#
   
    mat_dispo_trans = Materiel.query.with_entities(
        Materiel.nom_materiel,
        Materiel.nom_materiel).all()
    serv_dispo_trans = Service.query.with_entities(
        Service.nom_service,
        Service.nom_service).all()
    tt_le_mat_dispo = []
    # seul service à l'origine d'un trans == service informatique 
    le_serv_orig =[('Stocks Informatique','Stocks Informatique')]
    ls_serv_dest=[('Stocks Informatique','Stocks Informatique')]
    tt_le_mat_dispo += mat_dispo_trans
    ls_serv_dest += serv_dispo_trans
   
    transferer_materiel.nommaterieltransfere.choices = tt_le_mat_dispo
    transferer_materiel.originematerieltransfere.choices = le_serv_orig
    transferer_materiel.destinationmaterieltransfere.choices = ls_serv_dest
    ### Importer raisons transfert
    transferer_materiel.raisonmaterieltransfere.choices = raisons_transfert
    
    ##################################################################
    ### Si l'utilisateur valide un transfert  (via submit button) ####
    ##################################################################
    if transferer_materiel.validate_on_submit() and request.method == 'POST' :
        timestamp = datetime.datetime.now()
        check_si_transfert = checker(
            transferer_materiel.originematerieltransfere.data,
            transferer_materiel.destinationmaterieltransfere.data,
            transferer_materiel.nommaterieltransfere.data,
            transferer_materiel.quantitematerieltransfere.data,
            transferer_materiel.raisonmaterieltransfere.data)
        # la fonction checker() revoit un False
        if check_si_transfert == False:
            flash(f'Réessayez avec une quantité inférieure\
                  aux stocks disponibles', 'danger')
        # la fonction checker() revoit 'identique'
        elif check_si_transfert == 'identiques':
            flash(f"L'origine et la destination ne peuvent pas être \
                  identiques", 'danger')
        # la fonction checker() revoit 'pas de materiel'
        elif check_si_transfert == 'pas de materiel':
            flash(f'Pas assez de matériel en stock pour ce service.\
                  Veuillez ajouter du stock',
                  'danger')
        # la fonction checker() revoit un True
        elif check_si_transfert == True:
            flash(f"Cette opération n'est pas possible",'danger')
        # la fonction checker ne revoit rien, on peut efectuer un transfert
        else:
            # nom de materiel transf
            n_mat = transferer_materiel.nommaterieltransfere.data
            # qte transf
            qte = transferer_materiel.quantitematerieltransfere.data
            px_unit = float(
                Materiel.query.filter_by(
                    nom_materiel=n_mat).first().prix_unitaire)
            # puis on le multiplie par la qté pr avoir le coût
            ct_trans = qte * px_unit
            
            transf = Transfert(
                horodatage_transfert=timestamp,
                origine_transfert=transferer_materiel.originematerieltransfere.data,
                destination_transfert = transferer_materiel.destinationmaterieltransfere.data,
                nom_produit_transfert=transferer_materiel.nommaterieltransfere.data,
                quantite_transfert=transferer_materiel.quantitematerieltransfere.data,
                cout_transfert=ct_trans,
                raison_transfert=transferer_materiel.raisonmaterieltransfere.data)
            
            #Puis on met à jour Materiel pour avec la nlle valeur du stock
            ajout_valeur_stock()
            
            db.session.add(transf)
            db.session.commit()
            flash(f'Votre transfert a été ajouté!', 'success')
        return redirect(url_for('transfert'))
    return render_template(
        'transfert.html',
        title = 'Transfert',
        transferer_materiel = transferer_materiel,
        tous_les_transferts = tous_les_transferts)

def checker(origine_a_checker,
          destination_a_checker,
          nom_a_checker,
          qte_a_checker,
          raison_a_checker):
    '''
    checker() a pour but de verifier si un transfert de materiel est possible
    On peut determiner 4 cas de figure :
        1) checker() renvoie False:
                TRANSFERT IMPOSSIBLE
                Le stock de materiel du service à l'origine du transfert
                n'est pas assez important pour realiser l'opération
        
        2) checker() renvoie 'identique':
                TRANSFERT IMPOSSIBLE
                L'utilisateur a selectionné le même service pour l'origine
                et la destination du transfert.
                exemple: Urgences -> Urgences 
                
        3) checker() renvoie un True:
                TRANSFERT IMPOSSIBLE
                Car l'opération souaitée n'est pas valide
                    
        4) checker() ne revoie rien:
                TRANSFERT POSSIBLE
                
    '''
    # ************************************************************ #
    # ***************   ORIGINE == DESTINATION   ***************** #
    # ************************************************************ #
    #______________________________________________________________#
    ###############  PAS TRANSFERT  ################################
    #### checker() == 'identiques'##################################
    if origine_a_checker == destination_a_checker :
        identique = 'identiques'
        return identique
    #______________________________________________________________#
    # ********************************************************************** #
    # ** ORIGINE == 'Stocks Informatique' && DESTINATION == Autre service ** #
    # ********************************************************************** #    
    
    elif origine_a_checker =='Stocks Informatique' and destination_a_checker != 'Stocks Informatique':
        mat_dispo = Materiel.query.filter_by(
            nom_materiel=nom_a_checker).first()
        ###############  TRANSFERT OK  #################################
        # Si qté stocks disponible >= qté transférée
        if mat_dispo.qte_materiel >= qte_a_checker:
            mat_dispo.qte_materiel-= qte_a_checker
            mat_destocke = Materiel_destocke.query.filter_by(
                destination_destockage=destination_a_checker,
                nom_mat_destocke=nom_a_checker).first()
            ecq_mat_des = str(mat_destocke)
            # Si jamais aucun matériel n'a été transféré
            # autrement dit si Materiel_destocke est vide
            if(ecq_mat_des=='None'):
                #On stocke le px du materiel concerné dans px_mat
                px_mat = float(Materiel.query.filter_by(
                    nom_materiel=nom_a_checker).first().prix_unitaire)
                # puis on le multiplie par la qté pr avoir le coût
                ct_desto = qte_a_checker * px_mat
                mat_destocke_ajoute = Materiel_destocke(
                    nom_mat_destocke=nom_a_checker,
                    destination_destockage=destination_a_checker,
                    quantite_destockage=qte_a_checker,
                    cout_destockage=ct_desto,
                    raison_destockage=raison_a_checker)
                db.session.add(mat_destocke_ajoute)
            # si Materiel_destocke n'est pas vide
            else:
                mat_destocke.quantite_destockage += qte_a_checker
            db.session.commit()
        #______________________________________________________________#
        ###############  PAS TRANSFERT  ################################
        # Si qté de stocks disponible < qté de stocks transférée
        else :
            return False
        #______________________________________________________________#       
    # ********************* #
    # ** Autre operation ** #
    # ********************* #
    else:
        return True
    
# Materiel Destocké ---------------------------------------------------------
@app.route("/Materiel_destocke")
def materiel_destocke():
    tout_le_mat_destocke = Materiel_destocke.query.all()
    ecq_destockage = bool(Materiel_destocke.query.all())
    if ecq_destockage == False :
        flash(f'Veullez ajouter du materiel, des services ainsi que\
              des transferts pour les visualiser','info')
        return render_template(
            'materiel_destocke.html')
    else:
        return render_template(
            'materiel_destocke.html',
            tout_le_mat_destocke=tout_le_mat_destocke)