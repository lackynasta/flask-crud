# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
@app.route('/api/v1/produits')
def show_products():
    PRODUCTS = [{ 'id': 1, 'name': 'Skello' },{ 'id': 2, 'name': 'Socialive.tv' }]
    return jsonify(PRODUCTS)

