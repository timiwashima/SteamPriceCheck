# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 13:08:29 2023

@author: tiwashima
"""

import requests
from bs4 import BeautifulSoup

request=requests.get('https://store.steampowered.com/app/1364780/Street_Fighter_6/')

content=request.content
soup=BeautifulSoup(content, 'html.parser')
element=soup.find('div',{'class':'game_purchase_price price'})

price=element.text.strip()
priceNoCurrency=float(price[1:])

if priceNoCurrency<=20:
    print("The game is on sale for $20 or less.  You should buy it.")
else:
    print("The game is more than you want to spend.  You can wait for a sale.")