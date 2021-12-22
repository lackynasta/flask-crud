# wsgi.py
# pylint: disable=missing-docstring
from flask import Flask
from flask import jsonify
from flask import abort

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
