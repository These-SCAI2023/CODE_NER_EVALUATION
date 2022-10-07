#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 17:23:48 2021

@author: antonomaz
"""

import json
import re
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

import glob

def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)
        
        return dist
    
def nom_repertoire(chemin):
    for mot in glob.glob(chemin): 
        noms_rep = re.split("/", chemin)
        noms_repo = re.split("_",noms_rep[5])
        noms_repo = re.split("_",noms_repo[-1])
        noms_repo ="".join(noms_repo)
#        print("NOM FICHIER",noms_fichiers)

        return noms_repo

def nom_mod(path):
    for mot in glob.glob(path): 
        noms_mod = re.split("/", path)
        noms_mods = re.split("_",noms_mod[6])
        nm = re.split("_",noms_mods[-2])
        nmod ="".join(nm)
        return nmod
    

def diagramme_venn(liste_en_pp, liste_en_ocr):
    venn2([set(liste_en_pp), set(liste_en_ocr)],set_labels = ('NE Ref', 'NE OCR'))
    
    
     
def stocker(nom_fichier):
    plt.rcParams.update({'font.size': 16})
    plt.savefig(nom_fichier)
    plt.clf()
    
    return nom_fichier
    



        
path_corpora = "../output_corpora/corpora_EN_CONCAT_JSON_16032022/*/*/*/"
# dans "corpora" un subcorpus = toutes les versions 'un texte'

liste_EN_ocr=[]
liste_EN_pp=[]
#for subcorpus in sorted(glob.glob("%s/*"%path_corpora)):
for subcorpus in sorted(glob.glob(path_corpora)):
#    print(subcorpus)
    for path in sorted(glob.glob("%s/*.json"%subcorpus)):
#        print("subsubcorpus",path )
    
        texte = lire_fichier(path)
    #    print("************",subcorpus)
    #    print(texte)
        nomrep=nom_repertoire(path)
    #    print(nomrep)
        
        if nomrep == "PP" :        
            liste_EN_pp.append(path)
    #        liste_texte_pp.append(subcorpus)
            liste_EN_pp.append(texte)
              
        elif nomrep == "MOD":
            liste_EN_ocr.append(path)
    #         liste_texte_ocr.append(subcorpus)
            liste_EN_ocr.append(texte)
    
    
liste_ocr_verif=[] 
liste_pp_verif=[] 
i=0      
while i <len(liste_EN_ocr) :
    nom_mod_ocr=nom_mod(liste_EN_ocr[i])
#    print(nom_mod_ocr)
    nom_mod_pp=nom_mod(liste_EN_pp[i])
#    print(nom_mod_ocr)
    liste_ocr_verif.append(nom_mod_ocr)
    liste_pp_verif.append(nom_mod_pp)
    i=i+2
print(liste_ocr_verif)
print(liste_pp_verif)

result=True
for j in range(0,len(liste_ocr_verif)):
    if liste_ocr_verif[j]!=liste_pp_verif[j]:
        result = False
k=0
if result != False:
    while k<len(liste_EN_pp) :
        
        diagramme_venn(liste_EN_pp[k+1],liste_EN_ocr[k+1])
        stocker("%s_intersection.png"%liste_EN_ocr[k])
        k=k+2
       
    
else:
    print("NOT OK")
 
#    
#    
#
##        
##        print(subcorpus)
##print(liste_texte_pp)
##print(liste_texte_pp)
#print("EN PP 1**************** ",liste_EN_pp[0])
##print("EN PP 2**************** ",liste_EN_pp[1])
#print("EN PP 3**************** ",liste_EN_pp[2])
##print("EN PP 1**************** ",liste_EN_pp[3])
#print("EN PP 2**************** ",liste_EN_pp[4])
##print("EN PP 3**************** ",liste_EN_pp[5])
#print("EN OCR 1**************** ",liste_EN_ocr[0])
##print("EN OCR 2**************** ",liste_EN_ocr[1])
#print("EN OCR 3**************** ",liste_EN_ocr[2])
##print("EN OCR 1**************** ",liste_EN_ocr[3])
#print("EN OCR 2**************** ",liste_EN_ocr[4])
##print("EN OCR 3**************** ",liste_EN_ocr[5])


          


    
    
    