import re
import glob
import spacy
import json
import os
import shutil
import warnings
warnings.simplefilter("ignore")
#TODO: gérer warnings
from generic_tools import *
from optparse import OptionParser

def get_parser():
    """Returns a command line parser
    Returns:
        OptionParser. The command line parser
    """
    parser = OptionParser()
    parser.add_option("-d", "--data_path", dest="data_path",
                      help="""Chemin vers les fichiers txt (exemple DATA/*)""", type="string", default="DATA/")
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

def liste_resultats(texte, nlp =""):
    #nlp=spacy.load("fr_core_news_sm")):
    if nlp == "":
      try:
        nlp = spacy.load("fr_core_news_sm")
      except:
        cmd = "python3 -m spacy download fr_core_news_sm"
        os.system(cmd)
        nlp = spacy.load("fr_core_news_sm")
        
    doc = nlp(texte)
    list_resultats =[]
    for ent in doc.ents:
        if ent.label_=="LOC":
            list_resultats.append(ent.text)
    return (list_resultats)

for modele in ["sm", "md", "lg"]:
    liste_subcorpus = glob.glob("%s/*/"%path_corpora)
    if len(liste_subcorpus)==0:
      print(f"Pas de dossier trouvé dans {path_corpora}, traitement terminé")
      exit()
    print("Starting with modèle %s"%modele)
    nom_complet_modele = "fr_core_news_%s"%modele
    try:
        nlp = spacy.load(nom_complet_modele)
    except:
        cmd = f"python3 -m spacy download {nom_complet_modele}"
        os.system(cmd)
        nlp = spacy.load(nom_complet_modele)
    nom_modele = f"spacy-{modele}"

    for subcorpus in liste_subcorpus:
        print("  Processing %s"%subcorpus)
        liste_txt = glob.glob("%s/REF/*.txt"%subcorpus)
        liste_txt+=  glob.glob("%s/OCR/*/*.txt"%subcorpus)
        print("  nombre de fichiers txt trouvés :",len(liste_txt))
        for path in liste_txt: 
            dossiers  = re.split("/", path)[:-1]
            nom_txt = re.split("/", path)[-1]
            path_ner = "/".join(dossiers)+"/NER"
            os.makedirs(path_ner, exist_ok = True)
            path_output = "%s/%s_%s.json"%(path_ner, nom_txt, nom_modele)
            #path_output = f"{path_ner}/{nom_txt}_{nom_modele}.json"
            print(path_output)
            if os.path.exists(path_output)==True:
              if options.Force ==True:
                print("  Recomputing :",path_output)
              else:
                print("Already DONE : ", path_output)
                continue
            texte = lire_fichier(path)
            entites = liste_resultats(texte, nlp)
            stocker(path_output, entites, is_json=True)
        ### Penser à comment lancer compute_distances
