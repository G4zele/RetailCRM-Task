# coding utf-8

import retailcrm
import time
import json

client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
ID = '921'
exID = '1515147'
mode = 'serv'
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
    while n < len(result._Response__response_body['products']):
        ids.append(result._Response__response_body['products'][n]['id'])
        n += 1
    print(ids)
elif (mode == 'serv'):
    result = client.products({'externalId':exID})
    store_name = result._Response__response_body['products'][0]['url']
    if store_name.find('re-store.ru/catalog/') > -1:
        result = client.products({'name':'гарантии'})
        ids = []
        n = 0
        while n < len(result._Response__response_body['products']):
            ids.append(result._Response__response_body['products'][n]['id'])
            n += 1
        print(ids)

   