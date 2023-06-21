# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 07:06:38 2023

@author: tiwashima
"""
import requests
from bs4 import BeautifulSoup

games={
       'Street Fighter 6':
           {'url':'https://store.steampowered.com/app/1364780/Street_Fighter_6/',
            'desiredPrice':40},
       'Monster Hunter Rise':
           {'url':'https://store.steampowered.com/app/1446780/MONSTER_HUNTER_RISE/',
            'desiredPrice':20},
       'Kingdoms and Castles':
           {'url':'https://store.steampowered.com/app/569480/Kingdoms_and_Castles/',
            'desiredPrice':10}
       }

for gameTitle,steamGame in games.items():
    request=requests.get(steamGame['url'])
    desiredPrice=steamGame['desiredPrice']
    content=request.content
    soup=BeautifulSoup(content, 'html.parser')
    element=soup.find('div',{'class':'game_purchase_price price'})
    price=element.text.strip()
    priceNoCurrency=float(price[1:])
    if priceNoCurrency <= desiredPrice:
        print(gameTitle + ' is $' + str(priceNoCurrency) + '.')
