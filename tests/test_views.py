# tests/test_views.py
from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_read_many_products(self):
        response = self.client.get("/api/v1/produits")
        products = response.json
        self.assertIsInstance(products, list)
        #self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_read_product(self):
        response = self.client.get("/api/v1/produit/1")
        product = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(product, dict)
        self.assertEqual(product['name'], 'Skello')

    def test_delete_product(self):
        delete_response = self.client.delete("/api/v1/produit/3")
        deleted_product = delete_response.json
        self.assertEqual(delete_response.status_code, 204)
        self.assertIsNone(deleted_product)

        read_one_response = self.client.get("/api/v1/produit/3")
        read_one_product = read_one_response.json
        self.assertEqual(read_one_response.status_code, 404)
        self.assertIsNone(read_one_product)

    def test_delete_not_found_product(self):
        response = self.client.delete("/api/v1/products/20")
        product = response.json
        self.assertEqual(response.status_code, 404)
        self.assertIsNone(product)


