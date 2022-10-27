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
                      help="""Chemin vers les fichiers txt (exemple DATA/*)""", type="string", default="DATA/*/")
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


for path_auteur in glob.glob(f"{path_corpora}/*"):
  nom_auteur = re.split("/", path_auteur)[-1]
  print("-"*20)
  print(f"  Auteur traité : {nom_auteur}")
  
  dico_out, dist_txt = {}, {}
  liste_compare = []
  for file_type in ["txt"]:
    liste_txt_auteur = glob.glob("%s/*/*.%s"%(path_auteur, file_type))
    print(f"  NB {file_type} :", len(liste_txt_auteur))

    for path_file in liste_txt_auteur:
      # parsing nom de fichier 
      elems = re.split("_", re.split("/", path_file)[-1])
      auteur,titre, version = elems[:3]
      version = re.sub("\.txt", "", version)

      if file_type =="txt":
          liste_compare.append([version, lire_fichier(path_file)])
      else:
          nom_mod = re.sub("\.json", "", elems[-1])
          liste_compare.append([nom_mod,lire_fichier(path_file,True)])
          
  print("  Versions comparées : ",[x[0]for x in liste_compare])
  dico_out[file_type] = {}
  path_json = "%s_%s_distances.json"%(path_auteur, titre)
  if os.path.exists(path_json):
    if options.Force ==True:
      print("  Recomputing :",path_json)
    else:
      print("Already DONE : ", path_json)
      continue
  for ID1, version1 in enumerate(liste_compare):
      for ID2, version2 in enumerate(liste_compare[ID1+1:]):
          liste1 = liste_compare[ID1][1]
          liste2 = liste_compare[ID2][1]
          dico_dist = get_distances(liste1, liste2)
          paire = "%s--%s"%(version1, version2)
          dico_out[file_type][paire] = dico_dist
  
  stocker(path_json, dico_out, is_json=True, verbose = True)
    
