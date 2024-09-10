#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:43:26 2020

@author: jbt
"""

from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField,
                     SelectField, SubmitField, FloatField)
from wtforms.validators import (DataRequired, NumberRange)


class Ajoutermateriel(FlaskForm):
    nommateriel = StringField(
        'Nom du produit', validators=[DataRequired()])
    quantitemateriel = IntegerField(
        'Quantité', validators=[
        NumberRange(min=1, max=1000000),DataRequired()])
    prixmateriel = FloatField(
        'Prix Unitaire', validators=[
        NumberRange(min=1, max=1000000),DataRequired()])
    submitmateriel = SubmitField(
        'Enregistrer le materiel')

class Modifiermateriel(FlaskForm):
    modifnommateriel = StringField(
        'Nom du produit', validators=[DataRequired()])
    modifquantitemateriel = IntegerField(
        'Quantité', validators=[
        NumberRange(min=1, max=1000000),DataRequired()])
    modifprixmateriel = FloatField(
        'Prix Unitaire', validators=[
        NumberRange(min=1, max=1000000),DataRequired()])
    modifsubmitmateriel = SubmitField(
        'Enregistrer les changements')

class Ajouterservice(FlaskForm):
    nomservice = StringField(
        'Nom du Service', validators=[DataRequired()])
    submitservice = SubmitField(
        'Enregistrer le service')

class Modifierservice(FlaskForm):
    modifnomservice = StringField(
        'Nom du Service', validators=[DataRequired()])
    modifsubmitservice = SubmitField(
        'Enregistrer les changements')

class Transferermateriel(FlaskForm):
    nommaterieltransfere = SelectField(
        'Nom du Produit')
    originematerieltransfere = SelectField(
        'Origine')
    destinationmaterieltransfere = SelectField(
        'Destination')
    quantitematerieltransfere = IntegerField(
        'Quantité', validators=[NumberRange(
        min=1, max=1000000),DataRequired()])
    raisonmaterieltransfere = SelectField(
        'Raison')   
    submitmaterieltransfere = SubmitField(
        'Transferer')
    