#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 14:59:58 2021

@author: antonomaz
"""

import glob
import json
import re

def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)
    return dist

def stocker( chemin, contenu):

    w =open(chemin, "w")
    w.write(json.dumps(contenu , indent = 2))
    w.close()
    print(chemin)
    
    return chemin


#path_corpora = "../CORPORA/corpora_stanza_REN/*/*/*/*"
#path_corpora = "../corpora/corpora_test/*/*/*/*"
#path_corpora = "../CORPORA/corpora_stanza_REN/*/*/*"
path_corpora = "../WiNER_output/corpora/*/*/*/*.json"

for chemin in glob.glob(path_corpora):
    print(chemin)
    liste_EN = lire_fichier(chemin)
    list_concat =[]
    print(">>>>>>>>>>>>>CHEMIN",chemin)
#    print("**********LISTE EN********", liste_EN)
    
    for i in liste_EN:
        
        
        i_replace = i.replace(" ", "")
        
        list_concat.append(i_replace)
#    print(">>>>>>>>>>>>>CHEMIN",chemin)
#    print("LISTE EN REPLACE---------------",list_concat)
#    
    stocker("%s-concat.json"%(chemin), list_concat)




           
      















 
    