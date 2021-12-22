# wsgi.py
# pylint: disable=missing-docstring
from flask import Flask
from flask import jsonify
from flask import abort
from flask import request


app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Learn'},
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/produits', methods=['GET'])
def read_many_products():
    return jsonify(list(PRODUCTS.values()))

@app.route('/api/v1/produit/<int:product_id>', methods=['GET'])
def read_product(product_id):
    produit = {}
    for product in PRODUCTS.values():
        if product['id'] == product_id:
            produit = product
    if not produit:
        abort(404)
    return produit

@app.route('/api/v1/produit/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    produit = PRODUCTS.pop(product_id, None)
    if produit is None:
        abort(404)
    return '', 204

@app.route('/api/v1/produit', methods=['POST'])
def create_product():
    data = request.get_json()
    produits = list(PRODUCTS.values())
    last_product = produits[-1]
    last_id = last_product['id']
    next_id = last_id + 1

    if data is None:
        abort(401)
    name = data.get('name')
    if name is None:
        abort(400)
    if name == '' or not isinstance(name, str):
        abort(422)
    PRODUCTS[next_id] = {'id' : next_id , 'name' : name }

    return jsonify(PRODUCTS[next_id]), 201
