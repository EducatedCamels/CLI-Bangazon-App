import unittest
import sys;sys.path.append('../bangazon')
from CustomerManagement import *

class TestCustomerManagement(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.customer = {"first_name": "Meg", "last_name": "Ducharme", "address": "500 Interstate Blvd S", "phone_number": "4104561238"}
        self.payment_type = {"payment_type": "Visa", "account_number": "65ADF46ADG454"}

    def test_customer_is_saved_to_database(self):
        save_customer_to_database(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        customer_id = get_customer(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        self.assertIsNotNone(customer_id)

    def test_get_all_customers(self):
        save_customer_to_database(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        customer_list = get_all_customers()

        self.assertTrue(len(customer_list) > 0)

    def test_select_active_customer(self):
        save_customer_to_database(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])
     
        get_customer(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        select_active_customer(2)

        active_customer = get_active_customer()

        self.assertIsNotNone(active_customer)

    def test_create_payment_option(self):
        save_customer_to_database(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])
        customer_id = get_customer(self.customer["first_name"],self.customer["last_name"],self.customer["phone_number"],self.customer["address"])

        self.assertIsNotNone(customer_id)

        select_active_customer(2)

        active_customer = get_active_customer()

        self.assertIsNotNone(active_customer)

        save_payment_option_to_database(self.payment_type["payment_type"],self.payment_type["account_number"], active_customer)

        payment_id = get_payment_option(self.payment_type["payment_type"],self.payment_type["account_number"], active_customer)
        
        self.assertIsNotNone(payment_id)


if __name__ == '__main__':
    unittest.main()
