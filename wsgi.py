# wsgi.py
# pylint: disable=missing-docstring
from flask import Flask
from flask import jsonify
from flask import abort

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/produits')
def read_many_products():
    products = [{ 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    {'id': 3, 'name': 'Learn'}]
    return jsonify(products)

@app.route('/api/v1/produit/<int:product_id>')
def read_product(product_id):
    products = [{ 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    {'id': 3, 'name': 'Learn'}]
    produit = {}
    for product in products:
        if product['id'] == product_id:
            produit = product
    if not produit:
        abort(404)
    return produit
