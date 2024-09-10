#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creation des classes SQLAlchemy pour structurer et peupler la base de données
postgres 'hpe_informatique'.

___To do ____
Créer méthodes propre à chaque classe pour peupler bdd avec données aléatoires
ou réelles 
______________________________________________________________________________
"""

from app_stocks_info_hpe import db
from datetime import datetime


class Service(db.Model):
    id_service = db.Column(db.Integer, primary_key= True)
    nom_service = db.Column(db.String(500),unique = True, nullable = False)

    def __repr__(self):
        return f"Service('{self.id_service}','{self.nom_service}')"
        return "Service('{self.id_service}','{self.nom_service}')"

class Materiel(db.Model):
    id_materiel = db.Column(db.Integer, primary_key= True)
    nom_materiel = db.Column(db.String(50),unique = True ,nullable = False)
    qte_materiel = db.Column(db.Integer, nullable = False)
    prix_unitaire = db.Column(db.Float, nullable = False)
    valeur_stock = db.Column(db.Float, nullable = True)
    def __repr__(self):
        return f"Materiel('{self.id_materiel}','{self.nom_materiel}',\
            '{self.qte_materiel}')"

class Transfert(db.Model):
    id_transfert = db.Column(db.Integer, primary_key= True)
    horodatage_transfert = db.Column(db.DateTime, default=datetime.utcnow)
    origine_transfert = db.Column(db.String(50), nullable = False)
    destination_transfert = db.Column(db.String(50), nullable = False)
    nom_produit_transfert = db.Column(db.String(50), nullable = False)
    quantite_transfert = db.Column(db.Integer, nullable = False)
    cout_transfert = db.Column(db.Float, nullable = False)
    raison_transfert = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f"Transfert('{self.id_transfert}','{self.horodatage_transfert}'\
            ,'{self.origine_transfert}','{self.destination_transfert}'\
               ,'{self.quantite_transfert}')"

class Materiel_destocke(db.Model):
    id_mat_destocke = db.Column(db.Integer, primary_key= True,nullable = False)
    nom_mat_destocke = db.Column(db.String(50), nullable = False)
    destination_destockage = db.Column(db.String(500),nullable = False)
    quantite_destockage = db.Column(db.Integer, nullable = False)
    cout_destockage = db.Column(db.Float, nullable = False)
    raison_destockage = db.Column(db.String(500),nullable = False)
    def __repr__(self):
        return f"Materiel_destocke('{self.id_mat_destocke}',\
            '{self.nom_mat_destocke}','{self.destination_destockage}'\
                ,'{self.quantite_destockage}')"

# Metadonnées ---------------------------------------------------------------
#----------------------------------------------------------------------------
class Historique_achats(db.Model):
    id_histo = db.Column(db.Integer, primary_key= True)
    date_achat = db.Column(db.DateTime, default=datetime.utcnow)
    nom_achete = db.Column(db.String(50), nullable = False)
    qte_achetee = db.Column(db.Integer, nullable = False)
    prix_unit_ach = db.Column(db.Float, nullable = False)
    cout_achat = db.Column(db.Float, nullable = False)
    def __repr__(self):
        return f"Historique_achats('{self.id_histo}',\
            '{self.nom_mat_destocke}','{self.destination_destockage}'\
                ,'{self.quantite_destockage}')"

class Mat_effaces(db.Model):
    id_mat_eff =  db.Column(db.Integer, primary_key= True)
    date_eff_mat = db.Column(db.DateTime, default=datetime.utcnow)
    nom_mat_eff = db.Column(db.String(50), nullable = False)
    qte_mat_eff = db.Column(db.Integer, nullable = False)
    prix_unit_eff = db.Column(db.Float, nullable = False)
    valeur_stock_eff = db.Column(db.Float, nullable = False)
    def __repr__(self):
        return f"Mat_effaces('{self.id_mat_eff}',\
            '{self.nom_mat_eff}')"

class Serv_effaces(db.Model):
    id_serv_eff =  db.Column(db.Integer, primary_key= True)
    date_eff_serv = db.Column(db.DateTime, default=datetime.utcnow)
    nom_serv_eff = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f"Serv_effaces('{self.id_serv_eff}',\
            '{self.nom_serv_eff}')"

class Trans_effaces(db.Model):
    id_trans_eff =  db.Column(db.Integer, primary_key= True)
    date_eff_trans = db.Column(db.DateTime, default=datetime.utcnow)
    horo_trans_eff = db.Column(db.DateTime, default=datetime.utcnow)
    ori_trans_eff = db.Column(db.String(50), nullable = False)
    des_trans_eff = db.Column(db.String(50), nullable = False)
    nom_prod_trans_eff = db.Column(db.String(50), nullable = False)
    qte_trans_eff = db.Column(db.Integer, nullable = False)
    cout_trans_eff = db.Column(db.Float, nullable = False)
    raison_trans_eff = db.Column(db.String(50), nullable = False)
    def __repr__(self):
        return f"nom_serv_eff('{self.id_trans_eff}',\
            '{self.nom_prod_trans_eff}')"

#----------------------------------------------------------------------------
#----------------------------------------------------------------------------
