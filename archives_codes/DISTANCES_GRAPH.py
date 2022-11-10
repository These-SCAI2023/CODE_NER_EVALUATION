#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 12:25:50 2021

@author: antonomaz
"""


import glob , json, re

import matplotlib.pyplot as plt
import numpy as np


def lire_fichier (chemin):
    with open(chemin) as json_data: 
        dist =json.load(json_data)

    
    return dist

def nom_fichier(chemin):
    for mot in glob.glob(chemin): 
        noms_fichiers = re.split("/", chemin)
        nomsfich = re.split("\.",  noms_fichiers[5])
        nomsfich = re.split("_",  nomsfich[0])
        nmfich = nomsfich[0]
        
        return nmfich

def nom_version(chemin):
    for mot in glob.glob(chemin): 
        noms_versions = re.split("/", chemin)
        nomsvers = re.split("\.",  noms_versions[5])
        nomsvers = re.split("_",  nomsvers[0])
        nmversion = nomsvers[1]
        
        return nmversion

#def point_txt(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_txt, liste_name_metric):
def point_txt(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_txt,liste_name_metric) :
     
    x=["Tess-Fra","Tess-Fra-bin","Tess-png","Kraken"]
#    x=["Tess-Fra","Tess-bin","Tess-png","Kraken"]
    #Jaccard  = 1
    point_txt = [liste_tesseract_fra[0][0],liste_tesseract_frabn[0][0],liste_tesseract_png[0][0],liste_kraken_base[0][0] ] 
#    point_txt = [liste_tesseract_fra[0][0],liste_tesseract_bn[0][0],liste_tesseract_png[0][0],liste_kraken_base[0][0] ]
    plt.scatter(x, point_txt , label = (" ".join([liste_name_metric[0]," Ref. vs OCR Version"])), s=10, marker="s")

    #Braycurtis = 1
#    point_txt = [liste_tesseract_fra[0][1],liste_tesseract_bn[0][1],liste_tesseract_png[0][1],liste_kraken_base[0][1]]
    point_txt = [liste_tesseract_fra[0][1],liste_tesseract_frabn[0][1],liste_tesseract_png[0][1],liste_kraken_base[0][1]]
    plt.scatter(x, point_txt , label = (" ".join([liste_name_metric[1]," Ref. vs OCR Version"])), s=10, marker="s")

    ###DICE = 2
#    point_txt = [liste_tesseract_fra[0][2],liste_tesseract_bn[0][2],liste_tesseract_png[0][2],liste_kraken_base[0][2]]  
    point_txt = [liste_tesseract_fra[0][2],liste_tesseract_frabn[0][2],liste_tesseract_png[0][2],liste_kraken_base[0][2]]  
    plt.scatter(x, point_txt , label = (" ".join([liste_name_metric[2]," Ref. vs OCR Version"])), s=10, marker="s")
    
    #Cosinus = 3
#    point_txt = [liste_tesseract_fra[0][3],liste_tesseract_bn[0][3],liste_tesseract_png[0][3],liste_kraken_base[0][3]] 
    point_txt = [liste_tesseract_fra[0][3],liste_tesseract_frabn[0][3],liste_tesseract_png[0][3],liste_kraken_base[0][3]] 
    plt.scatter(x, point_txt , label = (" ".join([liste_name_metric[3]," Ref. vs OCR Version"])), s=10, marker="s")
    
    plt.ylabel("Distances")
    plt.xlabel("OCR Version")
    plt.axis([-1,4.5,0,1]) 


#def point_sm(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_sm, liste_name_metric):
def point_sm(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_sm,liste_name_metric):
     
    x=["Tess-Fra","Tess-Fra-bin","Tess-png","Kraken"]
#    x=["Tess-Fra","Tess-bin","Tess-png","Kraken"]
    #Jaccard  = 1
#    point_sm = [liste_tesseract_fra[1][0],liste_tesseract_bn[1][0],liste_tesseract_png[1][0],liste_kraken_base[1][0] ] 
    point_sm = [liste_tesseract_fra[1][0],liste_tesseract_frabn[1][0],liste_tesseract_png[1][0],liste_kraken_base[1][0] ] 
    plt.scatter(x, point_sm , label = (" ".join([liste_name_metric[0],dist_sm[-1]])), s=10, marker="s")
  
    #Braycurtis = 1
#    point_sm = [liste_tesseract_fra[1][1],liste_tesseract_bn[1][1],liste_tesseract_png[1][1],liste_kraken_base[1][1]]  
    point_sm = [liste_tesseract_fra[1][1],liste_tesseract_frabn[1][1],liste_tesseract_png[1][1],liste_kraken_base[1][1]]  
    plt.scatter(x, point_sm , label = (" ".join([liste_name_metric[1],dist_sm[-1]])), s=10, marker="s")
    
    ###DICE = 2
#    point_sm = [liste_tesseract_fra[1][2],liste_tesseract_bn[1][2],liste_tesseract_png[1][2],liste_kraken_base[1][2]]  
    point_sm = [liste_tesseract_fra[1][2],liste_tesseract_frabn[1][2],liste_tesseract_png[1][2],liste_kraken_base[1][2]]  
    plt.scatter(x, point_sm , label = (" ".join([liste_name_metric[2],dist_sm[-1]])), s=10, marker="s")

    #Cosinus = 3
#    point_sm = [liste_tesseract_fra[1][3],liste_tesseract_bn[1][3],liste_tesseract_png[1][3],liste_kraken_base[1][3]]  
    point_sm = [liste_tesseract_fra[1][3],liste_tesseract_frabn[1][3],liste_tesseract_png[1][3],liste_kraken_base[1][3]]  
    plt.scatter(x, point_sm , label = (" ".join([liste_name_metric[3],dist_sm[-1]])), s=10, marker="s")

    plt.ylabel("Distances")
    plt.xlabel("OCR Version")
    plt.axis([-1,4.5,0,1])  

#def point_md(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_md, liste_name_metric):
def point_md(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_md,liste_name_metric) :
    
#    x=["Tess-Fra","Tess-bin","Tess-png","Kraken"]
    x=["Tess-Fra","Tess-Fra-bin","Tess-png","Kraken"]

    #Jaccard  = 1
    
#    point_md = [liste_tesseract_fra[2][0],liste_tesseract_bn[2][0],liste_tesseract_png[2][0],liste_kraken_base[2][0]] 
    point_md = [liste_tesseract_fra[2][0],liste_tesseract_frabn[2][0],liste_tesseract_png[2][0],liste_kraken_base[2][0]] 
    plt.scatter(x, point_md , label = (" ".join([liste_name_metric[0],dist_md[-1]])), s=10, marker="s")
  
    #Braycurtis = 1
#    point_md = [liste_tesseract_fra[2][1],liste_tesseract_bn[2][1],liste_tesseract_png[2][1],liste_kraken_base[2][1]] 
    point_md = [liste_tesseract_fra[2][1],liste_tesseract_frabn[2][1],liste_tesseract_png[2][1],liste_kraken_base[2][1]]
    plt.scatter(x, point_md , label = (" ".join([liste_name_metric[1],dist_md[-1]])), s=10, marker="s")

    ###DICE = 2
#    point_md = [liste_tesseract_fra[2][2],liste_tesseract_bn[2][2],liste_tesseract_png[2][2],liste_kraken_base[2][2]]  
    point_md = [liste_tesseract_fra[2][2],liste_tesseract_frabn[2][2],liste_tesseract_png[2][2],liste_kraken_base[2][2]]  
    plt.scatter(x, point_md , label = (" ".join([liste_name_metric[2],dist_md[-1]])), s=10, marker="s")

    #Cosinus = 3
#    point_md = [liste_tesseract_fra[2][3],liste_tesseract_bn[2][3],liste_tesseract_png[2][3],liste_kraken_base[2][3]]  
    point_md = [liste_tesseract_fra[2][3],liste_tesseract_frabn[2][3],liste_tesseract_png[2][3],liste_kraken_base[2][3]]  
    plt.scatter(x, point_md , label = (" ".join([liste_name_metric[3],dist_md[-1]])), s=10, marker="s")

    plt.ylabel("Distances")
    plt.xlabel("OCR Version")
    plt.axis([-1,4.5,0,1]) 
    
#def point_lg(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_lg, liste_name_metric):
def point_lg(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_lg,liste_name_metric) :
    
    x=["Tess-Fra","Tess-bin","Tess-png","Kraken"]
#    x=["Tess-Fra","Tess-Fra-bin","Tess-png","Kraken"]
    #Jaccard  = 1
#    point_lg = [liste_tesseract_fra[3][0],liste_tesseract_bn[3][0],liste_tesseract_png[3][0],liste_kraken_base[3][0] ] 
    point_lg = [liste_tesseract_fra[3][0],liste_tesseract_frabn[3][0],liste_tesseract_png[3][0],liste_kraken_base[3][0] ] 
    plt.scatter(x, point_lg , label = (" ".join([liste_name_metric[0],dist_lg[-1]])), s=10, marker="s")
  
    #Braycurtis = 1
#    point_lg = [liste_tesseract_fra[3][1],liste_tesseract_bn[3][1],liste_tesseract_png[3][1],liste_kraken_base[3][1]]  
    point_lg = [liste_tesseract_fra[3][1],liste_tesseract_frabn[3][1],liste_tesseract_png[3][1],liste_kraken_base[3][1]]  
    plt.scatter(x, point_lg ,  label = (" ".join([liste_name_metric[1],dist_lg[-1]])), s=10, marker="s")

    ###DICE = 2
#    point_lg = [liste_tesseract_fra[3][2],liste_tesseract_bn[3][2],liste_tesseract_png[3][2],liste_kraken_base[3][2]] 
    point_lg = [liste_tesseract_fra[3][2],liste_tesseract_frabn[3][2],liste_tesseract_png[3][2],liste_kraken_base[3][2]]  
    plt.scatter(x, point_lg , label = (" ".join([liste_name_metric[2],dist_lg[-1]])), s=10, marker="s")

    #Cosinus = 3
#    point_lg = [liste_tesseract_fra[3][3],liste_tesseract_bn[3][3],liste_tesseract_png[3][3],liste_kraken_base[3][3]]  
    point_lg = [liste_tesseract_fra[3][3],liste_tesseract_frabn[3][3],liste_tesseract_png[3][3],liste_kraken_base[3][3]]  
    plt.scatter(x, point_lg ,  label = (" ".join([liste_name_metric[3],dist_lg[-1]])), s=10, marker="s")

    plt.ylabel("Distances")
    plt.xlabel("OCR Version")
    plt.axis([-1,4.5,0,1]) 

    

def stocker_graph_txt(nomfich): 
    
    name_fig = "%s.png"
    print(" nom de la figure ", name_fig)
#    
    plt.legend(loc="lower left",ncol=2, bbox_to_anchor=(-0.05,0.98))
    plt.legend 
    plt.savefig(nomfich)
    plt.clf()
    
    return nomfich

def stocker_graph(nomfich): 
    
    name_fig = "%s.png"
    print(" nom de la figure ", name_fig)
#    
    plt.legend(loc="lower left",ncol=2, bbox_to_anchor=(0.1,0.98))
    plt.legend 
    plt.savefig(nomfich)
    plt.clf()
    
    return nomfich




### MAIN

dist_txt=[]
dist_sm=[]
dist_md=[]
dist_lg=[]

liste_kraken_base =[]
liste_kraken_17 =[]
liste_tesseract_fra =[]
liste_tesseract_frabn =[]
liste_tesseract_png =[]
liste_tesseract_bn =[]
liste_name_metric=["Jaccard","Braycurtis","Dice","Cosinus"]


#path_corpora ="../NER_30062021/corpora_GRAPH_DIST_POINT_JSON/TESS-BIN/*"
path_corpora ="../NER_30062021/corpora_GRAPH_DIST_POINT_JSON/TESS-FRA-BIN/*"
for chemin in glob.glob(path_corpora):
    print ("***********CHEMIN",chemin)
    liste_kraken_base =[]
    liste_kraken_17 =[]
    liste_tesseract_fra =[]
    liste_tesseract_png =[]
    liste_tesseract_bn =[]
    liste_tesseract_frabn =[]

    for chemin_fichier in glob.glob("%s/*"%chemin):
#        print(chemin_fichier)
        path_dist=lire_fichier(chemin_fichier)
#        print(path_dist)
        nomfichier= nom_fichier(chemin_fichier)
        nomversion = nom_version(chemin_fichier)
#        print(chemin)
#        print(nomfichier)
#        print(nomversion)
#        print(path_corpora)
    
        dist_txt=[]
        dist_sm=[]
        dist_md=[]
        dist_lg=[]
        
#
#        
        version_OCR = nomversion
        print(version_OCR)
  
        modele_version = list(path_dist['json'].keys())
#        print("modele_version :",jsonversion)
        
        for cle, dic in path_dist.items(): 
#                
#            print("l'élément de clé", cle)
#            
#                
#                
            for version, modele in dic.items():
                for name_metric, liste in modele.items():
#                            liste_name_metric.append(name_metric)
                            
                            for resultat in liste:

                                if cle == "txt" :
                                    
                                    dist_txt.append(resultat)
                                   
                   
                                if version == "sm--sm" :
                                    
                                    dist_sm.append(resultat)

                                       
                                if version == "md--md" :
                                    
                                    dist_md.append(resultat) 
                                  
  
                                if version == "lg--lg":
                                    
                                    dist_lg.append(resultat)
                                    
                                    
        
        
        dist_txt.append("txt")
        dist_sm.append("sm")
        dist_md.append("md")
        dist_lg.append("lg")
#        print("-------SM",dist_sm)
#        print("--------MD",dist_md)
#        print("----------LG",dist_lg)        
#                
#        if version_OCR == "TESSERACT-BIN":
##
#            liste_tesseract_bn.append(dist_txt)
#            liste_tesseract_bn.append(dist_sm)
#            liste_tesseract_bn.append(dist_md)
#            liste_tesseract_bn.append(dist_lg)
#            print(version_OCR, liste_tesseract_bn)

            
#                
        if version_OCR == "TESSERACT-PNG":
            
            liste_tesseract_png.append(dist_txt)
            liste_tesseract_png.append(dist_sm)
            liste_tesseract_png.append(dist_md)
            liste_tesseract_png.append(dist_lg)
                
        if version_OCR == "TesseractFra-PNG":
           
            liste_tesseract_fra.append(dist_txt)
            liste_tesseract_fra.append(dist_sm)
            liste_tesseract_fra.append(dist_md)
            liste_tesseract_fra.append(dist_lg)
        
        if version_OCR == "TesseractFra-BIN":
            liste_tesseract_frabn.append(dist_txt)
            liste_tesseract_frabn.append(dist_sm)
            liste_tesseract_frabn.append(dist_md)
            liste_tesseract_frabn.append(dist_lg)
                
        if version_OCR == "kraken-base":
            
            liste_kraken_base.append(dist_txt)
            liste_kraken_base.append(dist_sm)
            liste_kraken_base.append(dist_md)
            liste_kraken_base.append(dist_lg)
        
#    

#    point_txt(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_txt,liste_name_metric)
    point_txt(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_txt,liste_name_metric)
    stocker_graph_txt("../NER_30062021/corpora_GRAPH_DIST_POINT_JSON/GRAPH-POINTS-29102021/%s-graph-dist-%s"%(nomfichier, dist_txt[-1])) 
    
#    point_sm(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_sm,liste_name_metric)
    point_sm(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_sm,liste_name_metric)
    stocker_graph("../NER_30062021/corpora_GRAPH_DIST_POINT_JSON/GRAPH-POINTS-29102021/%s-graph-dist-%s"%(nomfichier, dist_sm[-1])) 
#    
#    point_md(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_md,liste_name_metric)
    point_md(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_md,liste_name_metric)
    stocker_graph("../NER_30062021/corpora_GRAPH_DIST_POINT_JSON/GRAPH-POINTS-29102021/%s-graph-dist-%s"%(nomfichier, dist_md[-1])) 
##    
#    point_lg(liste_tesseract_fra,liste_tesseract_bn,liste_tesseract_png,liste_kraken_base, dist_lg,liste_name_metric)
    point_lg(liste_tesseract_fra,liste_tesseract_frabn,liste_tesseract_png,liste_kraken_base, dist_lg,liste_name_metric)
    stocker_graph("../NER_30062021/corpora_GRAPH_DIST_POINT_JSON/GRAPH-POINTS-29102021/%s-graph-dist-%s"%(nomfichier, dist_lg[-1]))     
#        

     
    

    
    
    
    