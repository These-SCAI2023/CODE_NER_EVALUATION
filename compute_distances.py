import re
import glob
import json
import os
import shutil
import warnings
warnings.simplefilter("ignore")
from generic_tools import *
from optparse import OptionParser

def get_parser():
    """Returns a command line parser
    Returns:
        OptionParser. The command line parser
    """
    parser = OptionParser()
    parser.add_option("-d", "--data_path", dest="data_path",
                      help="""Chemin vers les dossiers pour chaque livre (exemple DATA/*)""", type="string", default="DATA/*/")
    parser.add_option('-F', '--Force', help='Recalculer les distances même si déjà faites', action='store_true', default = False)
    return parser

parser = get_parser()
options, _ = parser.parse_args()
path_corpora = options.data_path

print("")
print("-"*40)
print(f"Path corpora : '{path_corpora}'")
print("--> pour spécifier un autre chemin utiliser l'option -d")
print("-"*40)

liste_txt = glob.glob(f"{path_corpora}/*/*/*.txt")
print("NB de txt trouvés", len(liste_txt))
liste_json = glob.glob(f"{path_corpora}/*/*/*.json")
print("NB de json trouvés", len(liste_json))
if len(liste_txt)==0:
  print("Aucun fichier txt trouvé.\n La structure des dossiers est probablement incorrecte, le répertoire doit être organisé comme suit : DOSSIER_LIVRE/Dossiersèversions")
  print("exiting....")
  exit()
#On exclut les JSON :
l_path_auteurs = [x for x in glob.glob(f"{path_corpora}/*") if "json" not in x]

for path_auteur in l_path_auteurs:
  nom_auteur = re.split("/", path_auteur)[-1]
  print("-"*20)
  print(f"  Auteur traité : {nom_auteur}")
  
  dico_out, dist_txt = {}, {}
  dic_compare = {}
  for file_type in ["txt", "json"]:
    dic_compare.setdefault(file_type, [])
    liste_txt_auteur = glob.glob("%s/*/*.%s"%(path_auteur, file_type))
    print(f"  NB {file_type} :", len(liste_txt_auteur))

    for path_file in liste_txt_auteur:
      # parsing nom de fichier 
      elems = re.split("_", re.split("/", path_file)[-1])
      auteur,titre, version = elems[:3]
      version = re.sub("\.txt", "", version)
      if file_type =="txt":
          dic_compare[file_type].append([version, lire_fichier(path_file)])
      else:
          nom_mod = re.sub("\.json", "", elems[-1])
          configuration = f"{version}_{nom_mod}"
          dic_compare[file_type].append([configuration,lire_fichier(path_file,True)])
          
  path_json = "%s_%s_distances.json"%(path_auteur, titre)
  if os.path.exists(path_json):
    if options.Force ==True:
      print("  Recomputing :",path_json)
    else:
      print("Already DONE : ", path_json)
      continue
  for file_type, liste_compare in dic_compare.items():
    print("  Versions (txt)/configurations (json) comparées : ",[x[0]for x in liste_compare])
    dico_out[file_type] = {}
    ID1 = 0
    for configuration1, content1  in liste_compare:
      if file_type=="json":
        version1, modele1 =re.split("_", configuration1)
      ID2 = ID1+1
      for configuration2, content2 in liste_compare[ID2:]:
          if file_type=="json":
            version2, modele2 =re.split("_", configuration2)
            if version1!=version2 and modele1!=modele2:#Comparaison sans sens
              continue
          liste1 = liste_compare[ID1][1]
          liste2 = liste_compare[ID2][1]
          dico_dist = get_distances(liste1, liste2)#TODO; json ?
          paire = "%s--%s"%(configuration1, configuration2)
          dico_out[file_type][paire] = dico_dist
          ID2+=1
      ID1+=1
  stocker(path_json, dico_out, is_json=True, verbose = True)
    
