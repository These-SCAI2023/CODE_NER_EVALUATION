#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 11:18:15 2023

@author: obtic2023
"""

import json
import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

def lire_fichier (chemin):
    with open(chemin) as json_data: 
        texte =json.load(json_data)
    return texte

tableau={}
liste_auteur=[]
liste_version=[]
liste_config=[]
liste_dist=[]
liste_name_metric=[]

liste_metric=["cosinus","jaccard"]
m=0

path_data="TGB_NER_SIM/*/OCR/*/NER/SIM/*.json"


for path_autor in glob.glob(path_data):
     #print(path_autor)

     distance = lire_fichier(path_autor)
     meta= path_autor.split("/")
     autor = meta[3].split("_")[0]
     #print(autor)
     liste_auteur.append(autor)
     version = meta[3].split("_")[1]
     #print(version)
     if version == "tesseract" or version == "TesseractFra-PNG":
         version = re.sub(version, "Tess. fr", version)
         print(version)
     if version == "tesseract-jspll-pretrain" or version == "TesseractFra-PNG-jspll-pretrain":
         version = re.sub(version, "Tess. fr -- jspl-fr", version)
         print(version)
     if version == "TesseractFra-PNG-jspll-ELTeC" :
         version = re.sub(version, "Tess. fr -- jspl-ELTeCfr", version)
         print(version)
     if version == "kraken" :
         version = re.sub(version, "Kraken", version)
         print(version)
     if version == "kraken-jspll-ELTeC" :
         version = re.sub(version, "Kraken -- jspl-ELTeCfr", version)
         print(version)
     if version == "kraken-jspll-pretrain" :
         version = re.sub(version, "Kraken -- jspl-fr", version)
         print(version)

     liste_version.append(version)
     config=meta[-1].split("_")[-1]
     config = config.split(".")[0]
     #print("**********",config)
     liste_config.append(config)


     for key, value in distance.items():
         if key == liste_metric[m]:
         #if key=="cosinus":
             liste_dist.append(value[0])
             #print(key,value)
         #if key == "jaccard":
             #print(key, value)

print(len(liste_auteur))
print(len(liste_version))
print(len(liste_config))
print(len(liste_dist))

tableau["Auteur"] = liste_auteur
tableau["Version"]=liste_version
tableau["Configuration"] = liste_config
tableau["Distance"] = liste_dist
#tableau["Metric"] = liste_name_metric
# tableau["Version_spacy"]=liste_version_spacy
data_tab = pd.DataFrame(tableau)
print(data_tab)
sns.set_theme(style="ticks")

# Initialize the figure with a logarithmic x axis
f, ax = plt.subplots(figsize=(7, 6))
ax.set_xscale("linear")
ax.set_xlim(0, 1)

# Plot the orbital period with horizontal boxes

#sns.boxplot(x="Distance", y="Version", data=data_tab, whis=[0, 1], width=.6, palette="vlag")
sns.boxplot(x="Distance", y="Version", data=data_tab, palette="vlag")

# Add in points to show each observation

sns.stripplot(x="Distance", y="Version", data=data_tab, size=4, color=".3", linewidth=0)

# Tweak the visual presentation
ax.xaxis.grid(True)
ax.set(ylabel="")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
sns.despine(trim=True, left=True)
plt.savefig("Boite-a-moustache_PNG/TGB_spacy-lg_%s.png"%liste_metric[m], dpi=300, bbox_inches="tight")
