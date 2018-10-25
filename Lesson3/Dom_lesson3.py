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


my_username = 'anthonyhoudaille'
my_tokenGit = 



def getSoupFromURL(url, method='get', data={}):
  if method == 'get':
    res = requests.get(url)
  ##elif method == 'post':
    ##res = requests.post(url, data=data)
  else:
    return None

  if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup
  else:
    return None


def getJson(Userpage):
    url_api = 'https://api.github.com' + Userpage
    r = requests.get(url_api, auth=(my_username, my_tokenGit))
    if r.status_code == 200:
        return r
    else:
        return None


def getUserInfoFromLine(line):
    
    #### INFO DE LA LIGNE DU TABLEAU
    
    rank = line.find('th', {'scope' : 'row'}).get_text()
    rank = int(rank[1:])  
    
    username = line.find('a').get_text()
    
    fullname = line.find('a').nextSibling
    if fullname:
        fullname = fullname[2:-1]  # pour enlever ' (' au début du nom et ')' à la fin
    
    nb_contribs = int(line.find_all('td')[1].get_text())
    
    location = line.find_all('td')[2].get_text()
    
    return [rank, username, fullname, nb_contribs, location]


def getNbReposNbStarsforUser(username, page):
    Userpage = '/users/' + username + '/repos?page=' + str(page) + '&per_page=100'  
    js = getJson(Userpage)
    if js != []:
        nb_repos = len(js)
        stars_list = [repo['stargazers_count'] for repo in js]
        return [nb_repos, sum(stars_list)]
    else:
        return [0, 0]




# main

start = time.time()

url_Contribs = 'https://gist.github.com/paulmillr/2657075'
soup = getSoupFromURL(url_Contribs)
lineoftr = soup.find('tbody').findChildren('tr')

df = pd.DataFrame(columns=['rank', 'username', 'fullname', 'contribs',
                           'location','nb_repo', 'total_stars'])

for line in lineoftr[:]:
    
    # Récupère infos du TopContributeurs via crawling de la page
    infos = getUserInfoFromLine(line)
    
    username = infos[1]
    
    # Récupère le nombre de repos et le nombre de Stars cumulées
    NbReposNbStars = getNbReposNbStarsforUser(username, 1)
    if NbReposNbStars[0] < 100:
        infos += NbReposNbStars
    else:  # API ne renvoie les infos que sur 100 repos max par requete
        page =2  # donc tant que la requete renvoie des repos, on continue à boucler
        while getNbReposNbStarsforUser(username, page)[0] != 0:
            NbReposNbStars[0] += getNbReposNbStarsforUser(username, page)[0]
            NbReposNbStars[1] += getNbReposNbStarsforUser(username, page)[1]
            page += 1
        infos += NbReposNbStars
    
    print(infos, '\n')
    df.loc[len(df)] = infos
    df.to_csv('./TopContribsData.csv', index=False)  
# on imprime les infos après chaque pour ne pas tout 
# au cas où il y ait un problème de serveur
    
    
# number Repo/stars mean:
#
df['stars/repo_mean'] = df.apply(lambda row: 0 if row['nb_repo']==0 
                                 else round(row['total_stars']/row['nb_repo'], 2), axis=1)

df.to_csv('./TopContribsData.csv', index=False)


# df sorted by mean Stars/Repos
# =======================================================
df_sorted = df.sort_values('stars/repo_mean', axis=0, ascending=False)
df_sorted.to_csv('./TopContribsData_sorted.csv', index=False)

print(df_sorted.head())

end = time.time()
totaltime = end - start
print('\n' + 'Time =', round(totaltime, 2), 's')