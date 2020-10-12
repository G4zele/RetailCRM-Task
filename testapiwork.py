import requests
import time

res1 = requests.get('https://popova.retailcrm.ru/api/v5/orders/history?&apiKey=h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
print(res1.text)

#res2 = requests.get('https://popova.retailcrm.ru/api/v5/integration-modules/recomendations/edit?&apiKey=h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')

#print(res2.text)


time.sleep(100)