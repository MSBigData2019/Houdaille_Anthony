#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:13:50 2018

@author: anthony
"""

## Crawling of www.reuters.com
## The goal is to return a CSV which is compose by 
    ## -The Quarter Sales (ending Dec-18)  --> OK
    ## -The price of the Action, and the %change at the moment where we scrawl the site --> OK
    ## -The % Shares Owned of institutional Holders --> OK
    ## -The Divident Yield of the company, industry and the sector --> OK
## We will chose LVMH, Airbus and Danone

import requests
from bs4 import BeautifulSoup

def Reuters() :
    Url = "https://www.reuters.com/finance/stocks/financial-highlights/"
    Query = ["LVMH", "AIR", "DANO"]
    
    for query in Query :
        
        r = requests.get(Url + query + ".PA")
        LVMH_html = r.text
        soup= BeautifulSoup(LVMH_html, 'html.parser')
        
        
        ActionDetail = soup.find("div", class_ = "sectionQuoteDetail")
        ActionPriceBrut = ActionDetail.find("span", attrs={'style':'font-size: 23px;'}).text
        ActionPrice = ActionPriceBrut.strip()
        
        ActionChange1 = soup.find("span", class_ = "valueContentPercent")
        ActionChangeBrut = ActionChange1.find("span", class_ = "pos" )
        
        if (ActionChangeBrut == None):
            ActionChangeBrut = ActionChange1.find("span", class_ = "neg" ).text.replace('(', '').replace(')', '')
        else :
            ActionChangeBrut = ActionChangeBrut.text.replace('(', '').replace(')', '')
        ActionChange = ActionChangeBrut.strip()
        
        Column1 = soup.find("div", class_ = "column1 gridPanel grid8")
        QuarterEnding = Column1.find("tr" , class_= "stripe").find_all("td", class_ = "data")
        QuarterEndingDec_18 = QuarterEnding[1].text.replace(",", " ").replace(".", " ")
        
        Column2 = soup.find("div", class_ = "column2 gridPanel grid4").find_all("div", class_="module")
        SharesOwner = Column2[3].find("tr" , class_= "stripe").find("td", class_ = "data").text
        
        DividentTable = Column1.find_all("div", class_ = "module")
        DividentYield = DividentTable[3].find("tr", class_="stripe").find_all("td", class_ = "data")
        DividentCompany = DividentYield[0].text
        DividentIndustry = DividentYield[1].text
        DividentSector = DividentYield[2].text
        
        
        print("The price of " + query +"'Action is " + ActionPrice + "€")
        print("The % of change for the action today is : " + ActionChange)
        print("The Quarter ending Dec_18 is : " + QuarterEndingDec_18 + "€")
        print("The % of Shares Owned for the institutional Holder is : " + SharesOwner )
        print("The Company'divident is : " + DividentCompany +"\nThe Industy'Divident is : "+ DividentIndustry +"\nThe Sector'Divident is : "+ DividentSector +"\n")