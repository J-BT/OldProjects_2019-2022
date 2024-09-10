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


def classement_cout_service():
    """ 
    Grâce à Pandas classe les services en fontion
    des coûts qu'ils ont générés.
    """   
    ls_transf = pd.read_sql_table('transfert', engine) 
    infos_bar_chart = ls_transf[["destination_transfert", "cout_transfert"]]
    cout_par_service = infos_bar_chart.groupby(
        ["destination_transfert"]).sum()
    
    cout_par_service.sort_values(by=["cout_transfert"],
                                 inplace=True,
                                 ascending=False)
    # print(cout_par_service)
    couts_serv = cout_par_service.to_dict(orient='dict')
    
    return couts_serv


###TESTS
CLASSEMENT_SERVICES_PAR_COUT = True

if __name__ == "__main__":
    
    if CLASSEMENT_SERVICES_PAR_COUT:
        classement = classement_cout_service()
        print(classement)
        