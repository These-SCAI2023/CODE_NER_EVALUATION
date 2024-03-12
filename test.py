from generic_tools import *

import glob
import re
import json
import sys
import os

def create_str_ner(json_path, str_path):
    """
    Transforme la liste d'entités en une string
    les mots des entités multi-mots sont concaténés
    """
    with open(json_path) as f:
        liste = json.load(f)
    liste = [re.sub("\s", "", x) for x in liste]
    with open(str_path, "w") as w:
        w.write(" ".join(liste))
