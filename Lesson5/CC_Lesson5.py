#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:49:25 2018

@author: anthonyhoudaille
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json
from pprint import pprint
import re



def getJson():
    url_api = 'https://open-medicaments.fr/api/v1/medicaments?query=parac%C3%A9tamol'
    r = requests.get(url_api)
    if r.status_code == 200:
        return r
    else:
        return None


# main

start = time.time()
Json = getJson()
df = pd.read_json(Json.content)

df = df.drop(["codeCIS"], axis = 1)
    #Utinisation du split
    #df["nom" , "labo", "Qte", "unité", "type"] = df["denomination"].str.split(" ")
    #df = df.drop(["denomination"], axis = 1)
    #print(df.head(5))

#utilisation d'un regex 
    #reg = r',(.*)' #recupère le type de médicament (gelule ou comprimé)
reg = r'([\D]*)(\d+)(.*),(.*)'#permet de séparer le premeir groupe de texte 
#(nom médoc + nom du labo) puis "\d+" dait référence a un int positif (quantité)
# puis on split par groupe de mot (unité) puis type
serie = df["denomination"]
ds = serie.str.extract(reg)
ds["mul"] = 1000
ds["mul"] = ds["mul"].where(ds[2].str.strip()== 'g', 1)
ds["dosage"] = ds[1].fillna(0).astype(int) * ds["mul"]
print (ds)
