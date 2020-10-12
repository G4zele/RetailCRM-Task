# coding utf-8

import retailcrm
import time
import json
from sys import argv

client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
site = 'example-com'

Product_name = 'Чехол' + ' ' + argv[1]
result = client.products({'name':Product_name})
print(result._Response__response_body)
jayson = json.dumps(result._Response__response_body)

