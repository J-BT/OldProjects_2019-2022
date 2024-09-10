#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 15:43:27 2020

@author: jbt
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

user = "utilisateur_hpe"
password = "bddhpe"
bd_name = "hpe_informatique"
host = "localhost"
port = 5432
URI = f"postgresql://{user}:{password}@{host}:{port}/{bd_name}"

# PENSER A BIEN NOTER -----> app.config['SQLALCHEMY_DATABASE_URI'] = {bdd}
app = Flask(__name__)
app.config['SECRET_KEY'] = '323b22caac41acbf'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
engine = create_engine(URI, echo=False)

from app_stocks_info_hpe import routes

db.create_all()
db.session.commit()
