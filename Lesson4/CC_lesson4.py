#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:35:44 2018

@author: anthonyhoudaille
"""

## Distance entre les 50 plus grandes villes de france

import requests
from bs4 import BeautifulSoup


url = "http://www.distance2villes.com/recherche?source="
ville_depart = "bordeaux"
urldistination = "&destination="
Ville_arrive= "paris"


r = requests.get(url +ville_depart + urldistination+ Ville_arrive)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

TxtTot = soup.find("p", attrs={'style':'clear:both'})
Distanceoiseau = TxtTot.find("strong", attrs={'id':'kmslinearecta'})
print(Distanceoiseau)
##print("Il y a " + Distanceoiseau + "de distance en voile d'oiseau entre" + ville_depart + "et" + Ville_arrive)

##