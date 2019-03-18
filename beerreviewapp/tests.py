from django.test import TestCase
from .models import Product, ProductType, Review
from .forms import ProductForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
# model tests

class BeerProductTest(TestCase):
    def test_stringOutput(self):
        product=Product(productname='Miller High Life')
        self.assertEqual(str(product), product.productname)

    def test_tablename(self):
        self.assertEqual(str(Product._meta.db_table), 'product')

class ProductTypeTest(TestCase):
    def test_stringOutput(self):
        techtype=ProductType(typename='Beer')
        self.assertEqual(str(techtype), techtype.typename)

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'producttype')

class ReviewTest(TestCase):
    def test_stringOutput(self):
        review=Review(reviewtitle='Miller High Life')
        self.assertEqual(str(review), review.reviewtitle)

    def test_tablename(self):
self.assertEqual(str(Review._meta.db_table), 'review')