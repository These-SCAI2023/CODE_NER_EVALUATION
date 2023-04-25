import json
import sklearn
from sklearn.neighbors import DistanceMetric
from sklearn.feature_extraction.text import CountVectorizer
import warnings
import re
from jiwer import wer
from jiwer import cer
from scipy.stats import entropy
import scipy

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
    if type(texte1) is list:
      texte1 = " ".join(texte1)
      texte2 = " ".join(texte2)
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
    scores2 = get_new_scores(texte1, texte2)
    for mesure_name, res in scores2.items():
      dico[mesure_name]=res
    return dico

##TODO: Fonction provenant de waddle: améliorer l'intégration
def get_new_scores(HYP_text, GT_text):
  scores= {}
  toto = ["precision", "recall", "f-score"]
  tokens_GT = re.findall("[a-zA-ZÀ-ÿ][a-zA-ZÀ-ÿ-]*", HYP_text)
  tokens_DET = re.findall("[a-zA-ZÀ-ÿ][a-zA-ZÀ-ÿ-]*", GT_text)
  GT_abs, GT_rel = get_voc(tokens_GT)
  DET_abs, DET_rel = get_voc(tokens_DET)
  voc_GT = set(GT_abs.keys())
  voc_DET = set(DET_abs.keys())
  dic = {"TP":len(voc_GT.intersection(voc_DET)),
         "FP":len(voc_DET.difference(voc_GT)),
         "FN":len(voc_GT.difference(voc_DET))}
  scores["voc_eval_res"] = {x: get_measures(dic)[x] for x in toto}
  scores["KL_res"] = {"KL divergence":get_Kullback(GT_rel, DET_rel),
                      "Euclidean Dist.":get_euclidean(GT_rel, DET_rel),
                      "WER": wer(" ".join(tokens_GT), " ".join(tokens_DET)),
                      "CER": cer(" ".join(tokens_GT), " ".join(tokens_DET)),
                      "Cosine Dist.":get_cosine(GT_rel, DET_rel)}
  dic2 = occ_eval(GT_abs,DET_abs)
  scores["occ_eval_res"] = {x: get_measures(dic2)[x] for x in toto}
  return scores
def get_voc(tokens):
  d_abs= {}
  for tok in tokens:
    d_abs.setdefault(tok, 0)
    d_abs[tok]+=1
  l = len(tokens)
  d_rel = {x:y/l for x, y in d_abs.items()}
  return d_abs, d_rel

def get_Kullback(dic1, dic2):
  smoothing = 0.00001#si une des probas est zero, KL est infini 
  vec1, vec2 =  dic2vec(dic1, dic2, smoothing)
  return entropy(vec1, qk=vec2)

def get_cosine(dic1, dic2):
  vec1, vec2 =  dic2vec(dic1, dic2, 0)
  return scipy.spatial.distance.cosine(vec1, vec2)

def get_euclidean(dic1, dic2):
  vec1, vec2 =  dic2vec(dic1, dic2, 0)
  return scipy.spatial.distance.euclidean(vec1, vec2)

def get_dice(dic1, dic2):
  vec1, vec2 =  dic2vec(dic1, dic2, 0)
  return scipy.spatial.distance.dice(vec1, vec2)

def dic2vec(dic1, dic2, smoothing=0): #TODO: improve with list comprehension
  L1, L2 = [], []
  for cle1, proba1 in dic1.items():
    L1.append(proba1)
    proba2 = smoothing
    if cle1 in dic2:
      proba2=dic2[cle1]
    L2.append(proba2)
  for cle2, proba2 in dic2.items():
    L2.append(proba2)
    proba1 = smoothing
    if cle2 in dic1:
      proba1 = dic1[cle2]
    L1.append(proba1)
  return L1, L2

def get_measures(dic, beta=1):
  """
  Computing measures from True Positives ....
  """
  TP, FP, FN = dic["TP"], dic["FP"], dic["FN"]
  if TP == 0:
      return {"recall": 0, "precision": 0, "f-score":0}
  R = 100*float(TP)/(TP+FN)
  P = 100*float(TP)/(TP+FP)
  B = beta*beta
  F = (1+B)*P*R/(B*P+R)
  return {"recall": round(R,4),"precision":round(P,4),"f-score": round(F, 4)}

def occ_eval(GT_abs, DET_abs):
  dic = {"TP":0, "FP":0, "FN":0}
  for cle, eff_GT in GT_abs.items():
    eff_DET = 0
    if cle in DET_abs:
      eff_DET = DET_abs[cle]
    FN = max(0, eff_GT-eff_DET)
    FP = max(0, eff_DET-eff_GT)
    dic["FN"] += FN
    dic["FP"] += FP
    dic["TP"] += eff_GT-FN
  for cle, eff_DET in DET_abs.items():
    if cle not in GT_abs:
      dic["FP"]+=eff_DET
  return dic
