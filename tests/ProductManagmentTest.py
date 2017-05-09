import unittest
import sys;sys.path.append('../bangazon')
from CustomerManagement import *
from ProductManagement import *

class TestProductManagement(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.customer = {"first_name": "Meg", "last_name": "Ducharme", "address": "500 Interstate Blvd S", "phone_number": "4104561238"}

        self.payment_type = {"payment_type": "Visa", "account_number": "65ADF46ADG454"}

        self.product = {"product_name": "unicorn pillow", "price": "$12.00"}

    # def test_product_is_saved_to_database(self):
    #     save_product_to_database(self.product["product_name"],self.product["price"])
    #
    #     product_id = get_product(self.product["product_name"],self.product["price"])
    #
    #     self.assertIsNotNone(product_id)
    #
    # def test_get_all_products(self):
    #     save_product_to_database(self.product["product_name"],self.product["price"])
    #
    #     product_list = get_all_products()
    #
    #     self.assertTrue(len(product_list) > 0)

    def test_add_product_to_order(self):
        save_customer_to_database(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        customer_id = get_customer(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        self.assertIsNotNone(customer_id)

        select_active_customer(2)
        active_customer = get_active_customer()
        self.assertIsNotNone(active_customer)

        save_product_to_database(self.product["product_name"],self.product["price"])
        product_id = get_product(self.product["product_name"],self.product["price"])

        self.assertIsNotNone(product_id)

        product_list = get_all_products()
        self.assertTrue(len(product_list) > 0)

        product_order_id = add_product_to_order(1, 2)
        self.assertIsNotNone(product_order_id)

    def test_complete_order(self):
        save_customer_to_database(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        customer_id = get_customer(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        self.assertIsNotNone(customer_id)

        select_active_customer(2)
        active_customer = get_active_customer()
        self.assertIsNotNone(active_customer)

        save_product_to_database(self.product["product_name"],self.product["price"])
        product_id = get_product(self.product["product_name"],self.product["price"])

        self.assertIsNotNone(product_id)

        product_order_id = add_product_to_order(active_customer, product_id)
        self.assertIsNotNone(product_order_id)

        active_order = get_active_order(active_customer)
        self.assertIsNotNone(active_order)

        save_payment_option_to_database(self.payment_type["payment_type"],self.payment_type["account_number"], active_customer)

        payment_id = get_payment_option(self.payment_type["payment_type"],self.payment_type["account_number"], active_customer)

        select_payment_option(1)

        is_complete = complete_order(payment_id, active_order)
