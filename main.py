import retailcrm
from flask import Flask, request

app = Flask(__name__)
client = retailcrm.v5('https://popova.retailcrm.ru', 'h1iKk1Sb0AaM66Ms86mXh7pgMaDz6wrN')

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/service')
def service():
    site = 'example-com'
    result = client.products({'name':'гарантии'})
    return result._Response__response_body
@app.route('/accessories')
def accessories():
    site = 'example-com' 
    Product_name = 'Чехол' + ' ' + request.args.get('accessorie')+','
    result = client.products({'name':Product_name})
    return result._Response__response_body
if __name__ == "__main__":
    app.run(debug=True)
