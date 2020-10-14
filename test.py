# coding utf-8

import retailcrm
import time
import json

client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
ID = 0
exID = 1515147
mode = 'access'
if (mode == 'access'):
    result = client.products({'externalId':exID})
    Product_name = result._Response__response_body['products'][0]['name']
    Product_name = (Product_name[Product_name.find(" ") + 1 : ])
    point = Product_name.find(",") + 1
    n = 0
    tmp = ""
    while n < point:
        tmp += Product_name[n]
        n += 1
    Product_name = tmp
    Product_name = 'Чехол ' + Product_name
    result = client.products({'name':Product_name})
    ids = []
    n = 0
    while n < 20:
        ids.append(result._Response__response_body['products'][n]['id'])
        n += 1
    print( {'by':'id', 'ids' : ids})
elif (mode == 'serv'):
    result = client.products({'name':'гарантии'})
    a.ids = []
    n = 0
    while n < 20:
        ids.append(result._Response__response_body['products'][n]['id'])
        n += 1
    print({'by':'id', 'ids' : ids})