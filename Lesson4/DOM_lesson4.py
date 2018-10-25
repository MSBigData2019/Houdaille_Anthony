#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:57:51 2018

@author: anthonyhoudaille
"""
#1°)recuperer une liste de voiture avec des attributs (age, prix, tel, vendeur, kmage )
#2°) checker le prix de l'argus en fct des années/kmage
#3°) Sortir la liste des voitures qui sont moins cher que l'argus.
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def LaCentrale():
    
    Tag = 'Acheter/'
    url = "https://www.lacentrale.fr/listing"
    url_model = "?makesModelsCommercialNames=RENAULT%3AZOE"
    url_page = "&options=&page="
    url_region = "&regions=FR-IDF%2CFR-PAC%2CFR-NAQ"
    url_sort = "&sortBy=priceAsc"
   
    r = requests.get(url + url_model + url_region+ url_sort)
    html_page1 = r.text
    soup = BeautifulSoup(html_page1)
    class_numAd = 'titleNbAds bold sizeC' #'numAnn'
    nbAds = soup.find("h2" , class_ = class_numAd).text
   
    print(nbAds)
    #numberOfPages = int(nbAds) / 16
    #print(numberOfPages)
    url2 = "https://www.lacentrale.fr/auto-occasion-annonce-69103272076.html"
 
    r2 = requests.get(url2)
    html = r2.text
    soup2 = BeautifulSoup(html , 'html.parser')
    val = soup2.find("strong" , class_ = "")
    
    print(val.text)
    if r.status_code == 200 :
        
        class_price = 'sizeD lH35 inlineBlock vMiddle' #Strong
        class_Kmage = 'clearPhone lH40' #span
        class_phone = 'bold' #span
        class2 ='fieldMileage'
        class_Saler = 'bold italic mB10' #div
        
        html_doc = r.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        all_links = soup.find("div", class2)
        print(all_links.text)
        #print([remise.text for remise in all_links])