import unittest
import sys;sys.path.append('../bangazon')
from ProductManagement import *

 @classmethod
    def setUpClass(self):
        self.customer = {"first_name": "Meg", "last_name": "Ducharme", "address": "500 Interstate Blvd S", "phone_number": "4104561238"}
        self.payment_type = {"payment_type": "Visa", "account_number": "65ADF46ADG454"}
        self.product = {"product_name": "unicorn pillow", "price": "$12.00"}

	def test_add_product_to_cart(self):
       save_customer_to_database(self.first_name,self.last_name,self.phone_number,self.address)
        customer_id = get_customer(self.first_name,self.last_name,self.phone_number, self.address)
        self.assertIsNotNone(customer_id)

        select_active_customer(2)
        self.assertIsNotNone(active_customer)

		product_list = get_all_products()
		self.assertTrue(len(product_list) > 0)

		product_id = get_product(self.product_name, self.price)

		add_product_to_cart(product_id)
		self.assertIn("unicorn pillow", add_product_to_cart)

