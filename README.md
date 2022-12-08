# Évaluation des performances de Reconnaissance d'entités nommées (REN) sur des transcriptions OCR bruitées.

Cet outil permet d'extraire les entités nommées (Use_spacy.py) d'un texte puis de calculer les distances (generic_tools et compute_distances.py) de Jaccard, Bray-Curtis, Dice et Cosinus entre la REN sur un texte de référence et sur les versions OCR d'un même texte.

Vous trouverez le corpus de texte sur dans le répertoire : (https://github.com/These-SCAI2023/NER_GEO_COMPAR) , RESULTATS_2021/DATA 

## UTILISATION

### REN : 
``` python Use_spacy.py -d "chemin" ``` 
(exemple DATA/*)

### Distances :

``` python compute_distances.py -d "chemin" ``` 
(exemple DATA/*)
