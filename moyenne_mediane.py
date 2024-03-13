#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:44:43 2024

@author: ceres
"""

import glob
import json
import numpy as np

def lire_fichier_json (chemin):
    with open(chemin) as json_data: 
        texte =json.load(json_data)
    return texte

def moyenne(liste_res):
    somme= sum(liste_res)
    moyenne=somme/len(liste_res)
    return(moyenne)

def mediane(liste_resm):
    a = np.array(liste_resm)
    median_value = np.percentile(a, 50)
    return median_value

def stocker_json(chemin,contenu):
    with open(chemin, "w", encoding="utf-8") as w:
        w.write(json.dumps(contenu, indent =2,ensure_ascii=False))
    return

liste_CERK=[]
liste_WERK=[]
liste_CERT=[]
liste_WERT=[]
dico_res={}
path_file="./DATA/*/*.json"
for file in glob.glob(path_file):
    print(file)
    data=lire_fichier_json(file)
    
    for key, value_dic in data.items():
        if key=="txt":
            for k, v in value_dic.items():
                print(k)
                if "PP--Kraken" in k or "PP--Kraken-base" in k or "Kraken-base--PP" in k:
                    dico_res["Kraken"]={}
                    for ssk, ssv in v.items():
                        if ssk == "KL_res":
                            for sssk,sssv in ssv.items():                                
                                if sssk =="CER":
                                    dico_res["Kraken"][sssk]={}
                                    #print(sssk,sssv)
                                    liste_CERK.append(sssv)
                                    moycerk=moyenne(liste_CERK)
                                    medcerk =mediane(liste_CERK)
                                    dico_res["Kraken"][sssk]["moy"]=moycerk
                                    dico_res["Kraken"][sssk]["med"]=medcerk
                                if sssk=="WER":
                                    dico_res["Kraken"][sssk]={}
                                    liste_WERK.append(sssv)
                                    moywerk=moyenne(liste_WERK)
                                    medwerk =mediane(liste_WERK)
                                    dico_res["Kraken"][sssk]["moy"]=moywerk
                                    dico_res["Kraken"][sssk]["med"]=medwerk
                if "PP--TesseractFra-PNG" in k or "TesseractFra-PNG--PP" in k:
                    dico_res["Tess. fra"]={}
                    for ssk, ssv in v.items():
                        if ssk == "KL_res":
                            for sssk,sssv in ssv.items():
                                if sssk =="CER":
                                    dico_res["Tess. fra"][sssk]={}
                                    #print(sssk,sssv)
                                    liste_CERT.append(sssv)
                                    moycert=moyenne(liste_CERT)
                                    medcert =mediane(liste_CERT)
                                    dico_res["Tess. fra"][sssk]["moy"]=moycert
                                    dico_res["Tess. fra"][sssk]["med"]=medcert
                                if sssk=="WER":
                                    dico_res["Tess. fra"][sssk]={}
                                    liste_WERT.append(sssv)
                                    moywert=moyenne(liste_WERT)
                                    medwert =mediane(liste_WERT)
                                    dico_res["Tess. fra"][sssk]["moy"]=moywert
                                    dico_res["Tess. fra"][sssk]["med"]=medwert
            stocker_json("./DATA/moy_mediane.json",dico_res)