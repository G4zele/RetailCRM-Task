# coding utf-8

import retailcrm
import time
import json

client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
site = 'example-com'

cfg = {
        'code':'testd',
        'integrationCode':'testd',
        'active':True,
        'name' : 'Сервисные программы и Аксессуары',
        'clientId':'10',
        'baseUrl' : 'http://80.76.42.209:5000',
        'actions' :
        {
            'accessories' : '/accessories?accessorie=',
            'service'  : '/service'
        },
        'integrations/recommendation/modes':
        {
                'code':'access',
                'names' : 
                        {
                           'ru' : 'Аксессуары',
                           'en' : 'Accessories',
                           'es' : ''
                        } 
        }
}
result = client.integration_module_edit(cfg)
print(result._Response__response_body)
clientid = client.integration_module('testd')
print(clientid._Response__response_body)
time.sleep(100)