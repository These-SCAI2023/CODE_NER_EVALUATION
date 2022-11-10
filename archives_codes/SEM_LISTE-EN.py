#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:29:40 2022

@author: antonomaz
"""


import spacy
import glob
import json

def lire_fichier(chemin): 
    lect = open(chemin, "r")
    chaine_lect = lect.read()
    lect.close()
    return chaine_lect

def stocker(chemin, contenu): 
    w = open(chemin, "w")
    w.write(json.dumps(contenu, indent=2))
    w.close()


liste_contenu=[]
liste_Entity = []
path_corpora = "../WiNER_output/corpora/*/*/*/"
# dans "corpora" un subcorpus = toutes les versions 'un texte'

for subcorpus in sorted(glob.glob(path_corpora)):
#    print(subcorpus)
    for path in sorted(glob.glob("%s*.ann"%subcorpus)):
        liste_contenu=[]
        liste_Entity =[]
#        print("****************************",path,"*******************************")
        
        contenu = lire_fichier(path)
#        print(contenu)
        liste_contenu = contenu.split("\n")
        print("****************************",path,"*******************************")    
#        print(liste_contenu[0])
        
        for ligne in liste_contenu:
            liste_ligne = ligne.split("\t")
            Label = liste_ligne[1]
            Entity=liste_ligne[-1]
            nb = liste_ligne[0]
            
            
#                print(i)
#            print(nb, Label, Entity)
            liste_label= Label.split(" ")
            Label = liste_label[0]
#            print(Label)
#            
            if Label == "Location":
                liste_Entity.append(Entity)
                
#                print(Label, nb, Entity)
        print(len(liste_Entity))
        stocker("%s_SEM.json"%path, liste_Entity )
            
            
        
       
        
        