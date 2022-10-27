import json
import sklearn
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
import warnings
warnings.simplefilter("ignore")

def lire_fichier (chemin, is_json = False):
    f = open(chemin , encoding = 'utf−8')
    if is_json==False:
      chaine = f.read()
    else:
      chaine = json.load(f)
    f.close ()
    return chaine

def stocker( chemin, contenu, is_json=False, verbose =False):
    if verbose==True:
      print(f"  Output written in {chemin}")
    w = open(chemin, "w")
    if is_json==False:
      w.write(contenu)
    else:
      w.write(json.dumps(contenu , indent = 2, ensure_ascii=False))
    w.close()
    


def get_distances(texte1, texte2, N=1, liste_name =["jaccard", "braycurtis","dice", "cosinus"] ):
    dico = {}
    for metric_name in liste_name :
        dico[metric_name] = []
        liste_resultat_dist2 = []
        for n_max in range(1, N+1):###range([min, default = 0], max, [step, default = 1]) 
            V = CountVectorizer(ngram_range=(1,n_max ), analyzer='char') 
            X = V.fit_transform([texte1, texte2]).toarray()
            if metric_name!= "cosinus" :  
                dist = DistanceMetric.get_metric(metric_name)     
                distance_tab1=dist.pairwise(X)
                liste_resultat_dist2.append(distance_tab1[0][1])
            else: 
                distance_tab1=sklearn.metrics.pairwise.cosine_distances(X) 
                liste_resultat_dist2.append(distance_tab1[0][1])
            dico[metric_name] = liste_resultat_dist2
    return dico
