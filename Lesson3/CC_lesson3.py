#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:33:34 2018

@author: anthonyhoudaille
"""

import requests
from bs4 import BeautifulSoup
def Remise() :
    Url = "https://www.darty.com/nav/recherche?s=relevence&text="
    Query = ["dell", "acer", "toshiba", "HP"]
    url2 = "&fa=756"
    finUrl = "&o="
    
    
    for query in Query :
        nbremise =0
        for nb in range(0,180, 30) :
            r = requests.get(Url + query +url2 + finUrl + str(nb))
            doc_html = r.text
            soup= BeautifulSoup(doc_html, 'html.parser')
            
            
            remise = soup.find_all('p', class_ = "darty_prix_barre_remise darty_small separator_top")
            
            nbremise = nbremise + len(remise)
        print(remise)    
        print("nombre de remise " + query + " :" + str(nbremise))
        #for nb in range()
        #r2 = requests.get(Url + query + page + nb +finUrl)
        #doc_html = r.text
        #soup= BeautifulSoup(doc_html, 'html.parser')
        
        
        #ActionDetail = soup.find("div", class_ = "sectionQuoteDetail")
        #ActionPriceBrut = ActionDetail.find("span", attrs={'style':'font-size: 23px;'}).text
        #ActionPrice = ActionPriceBrut.strip()
       
        
        
        #print("The Company'divident is : " + DividentCompany +"\nThe Industy'Divident is : "+ DividentIndustry +"\nThe Sector'Divident is : "+ DividentSector +"\n")
        
        