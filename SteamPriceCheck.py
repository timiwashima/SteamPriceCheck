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

prices={
        'Street Fighter 6':40,
        'Monster Hunter Rise':20,
        'Kingdoms and Castles':10
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
    
    for key in prices:
        if gameName==key:
            if priceNoCurrency<=prices[gameName]:
                print(gameName + ' is less than $' + str(prices[gameName]) + '.  You should buy it.')
            else:
                print(gameName + ' is more than $' + str(prices[gameName]) + '.  Wait for a sale.')
