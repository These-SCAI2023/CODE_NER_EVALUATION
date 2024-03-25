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
m=1


path_data="TGB_texte_SIM/*/*.json"

for path_autor in glob.glob(path_data):
     print(path_autor)
     data=lire_fichier(path_autor)

     for key, value in data.items():
         if key=="txt":

             for version, v in value.items():
                 if "REF" in version:

                    if version == "tesseract--REF" or version == "TesseractFra-PNG--REF":
                        version = re.sub(version, "Tess. fr", version)

                    if version == "tesseract-jspll-pretrain--REF" or version == "TesseractFra-PNG-jspll-pretrain--REF":
                        version = re.sub(version, "Tess. fr -- jspl-fr", version)

                    if version == "TesseractFra-PNG-jspll-ELTeC--REF":
                        version = re.sub(version, "Tess. fr -- jspl-ELTeCfr", version)

                    if version == "kraken--REF":
                        version = re.sub(version, "Kraken", version)

                    if version == "kraken-jspll-ELTeC--REF":
                        version = re.sub(version, "Kraken -- jspl-ELTeCfr", version)

                    if version == "kraken-jspll-pretrain--REF":
                        version = re.sub(version, "Kraken -- jspl-fr", version)

                    liste_version.append(version)
                    for kk, vv in v.items():
                        if kk==liste_metric[m]:
                            liste_dist.append(vv[0])
#print("liste_version***********",liste_version)
#tableau["Auteur"] = liste_auteur
tableau["Version"]=liste_version
#tableau["Configuration"] = liste_config
tableau["Distance"] = liste_dist
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
plt.savefig("Boite-a-moustache_PNG/TGB-texte-SIM_%s.png"%liste_metric[m], dpi=300, bbox_inches="tight")