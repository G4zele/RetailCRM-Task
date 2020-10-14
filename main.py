import retailcrm
from flask import Flask, request

app = Flask(__name__)
client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')
class Answer:
    by = 'id'
    ids = []

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/testd')
def service():
    a = Answer
    ID = request.args.get('ids%5B0%5D=')
    exID = request.args.get('externalIds%5B0%5D=')
    mode = request.args.get('mode=')
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
        a.ids = []
        n = 0
        while n < result._Response__response_body['pagination']['totalCount']:
            a.ids.append(result._Response__response_body['products'][n]['id'])
            n += 1
        return a
    elif (mode == 'serv'):
        result = client.products({'name':'гарантии'})
        a.ids = []
        n = 0
        while n < result._Response__response_body['pagination']['totalCount']:
            a.ids.append(result._Response__response_body['products'][n]['id'])
            n += 1
        return a

   
    

if __name__ == "__main__":
    app.run(debug=True)
