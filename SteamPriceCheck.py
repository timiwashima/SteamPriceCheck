# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:08:29 2023

@author: tiwashima
"""

import requests
from bs4 import BeautifulSoup

games={
       'Street Fighter 6':'https://store.steampowered.com/app/1364780/Street_Fighter_6/',
       'Monster Hunter Rise':'https://store.steampowered.com/app/1446780/MONSTER_HUNTER_RISE/',
       'Kingdoms and Castles':'https://store.steampowered.com/app/569480/Kingdoms_and_Castles/'
       }

for game,url in games.items():
    gameName=game
    gameURL=url
    
    request=requests.get(gameURL)
    content=request.content
    soup=BeautifulSoup(content, 'html.parser')
    element=soup.find('div',{'class':'game_purchase_price price'})
    price=element.text.strip()
    priceNoCurrency=float(price[1:])

    if gameName=='Street Fighter 6':
        if priceNoCurrency<=20:
            print(gameName + ' is less than $20.  You should buy it.')
        else:
            print(gameName + " is more than you want to spend.  Wait for a sale.")
    if gameName=='Monster Hunter Rise':
        if priceNoCurrency<=20:
            print(gameName + ' is less than $20.  You should buy it.')
        else:
            print(gameName + ' is more than you want to spend.  Wait for a sale.')
    if gameName=='Kingdoms and Castles':
        if priceNoCurrency<=10:
            print(gameName + ' is less than $10.  You should buy it.')
        else:
            print(gameName + ' is more than you want to spend.  Wait for a sale.')
