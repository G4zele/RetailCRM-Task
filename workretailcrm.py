# coding utf-8

import retailcrm
import time
import json

client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
site = 'example-com'

mod = {
        'code':'testd', 
        'name' : 'Аксессуары и сервисные программы',
        'baseUrl' : 'http://127.0.0.1:8000',
        'clientId':'10',
        '/integrations/recommendation/modes':{
                        'code':'access',
                        'names': 
                        [   
                            {'ru' : 'Сервисные программы',
                            'en' : 'Service programs',
                            'es' : ''}
                        ]
        }
}
                    #{
                    #    'code':'access',
                    #    'names' : 
                    #            {
                    #               'ru' : 'Аксессуары',
                    #               'en' : 'Accessories',
                    #               'es' : ''
                    #            },
                    #}

        #'actions' : [
        #                {
        #                    'mpartner':'partner.py',
        #                        
        #                },
        #                {
        #                    'maccess':'access.py',
        #                }
        #            ],

result = client.integration_module_edit(mod)
print(result._Response__response_body)
clientid = client.integration_module('testd')
print(clientid._Response__response_body)
time.sleep(100)