#!/usr/bin/env python3
# -*- coding: utf-8 -*-

############
# Services #
############
import pandas as pd

services =[
    ('Ambulatoire (BOX ou LIT)'),
    ('Geriatrie (1A)'),
    ('Chirurgie Ortho. - Plastie - Ophtalmo. (1B)'),
    ('Gastro-Enterologie - Neurologie (2A)'),
    ('Cardiologie - Nephrologie (2B)'),
    ('USIC - 2D'),
    ('Oncologie - Pneumologie (3A)'),
    ('Vasculaire - Thoracique - Urologie - ORL (3B)'),
    ('Chirurgie Digestive - Gynecologie (3C)'),
    ('Maternite (3D)'),
    ('Dialyse'),
    ('Urgences - US'),
    ('USC')
    ]

def generation_de_services():
    service_a_inserer = {}
    id_provisoire = 0
    
    for service in services:
        ligne_pour_bdd = []
        serv_name = service
        ligne_pour_bdd.append(serv_name)
        service_a_inserer[id_provisoire] = ligne_pour_bdd
        id_provisoire += 1
    
    return pd.DataFrame.from_dict(service_a_inserer, orient='index')


#####################
# Raisons Transfert #
#####################

# Pour selecteur
# raisons_transfert =[
#     'Vol',
#     'Casse',
#     'Defectueux',
#     'Mise a niveau'
#     ]

raisons_transfert = [('Casse','Casse'),
                     ('Vol','Vol'),
                     ('Defectueux','Defectueux'),
                     ('Mise a niveau','Mise a niveau')]


if __name__ == '__main__':
    a = generation_de_services()
        
    # for service in services:
    #     ajout_dans_service=Location(
    #         loc_name=service)
    #     db.session.add(ajout_dans_service)
    # db.session.commit()
    
