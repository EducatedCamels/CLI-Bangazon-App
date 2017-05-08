import unittest
import sys;sys.path.append('../bangazon')
from CustomerManagement import *

class TestCustomerManagement(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.customer = {"first_name": "Meg", "last_name": "Ducharme", "address": "500 Interstate Blvd S", "phone_number": "4104561238"}
        self.payment_type = {"payment_type": "Visa", "account_number": "65ADF46ADG454"}

    def test_customer_is_saved_to_database(self):
        save_customer_to_database(self.first_name,self.last_name,self.phone_number,self.address)

        customer_id = get_customer(self.first_name,self.last_name,self.phone_number, self.address)

        self.assertIsNotNone(customer_id)

    def test_get_all_customers(self):
        save_customer_to_database(self.first_name,self.last_name,self.phone_number,self.address)

        customer_list = get_all_customers()

        self.assertTrue(len(customer_list) > 0)

    def test_select_active_customer(self):
        
        save_customer_to_database(self.first_name,self.last_name,self.phone_number,self.address)
        get_customer(self.first_name,self.last_name,self.phone_number, self.address)

        select_active_customer(2)

        self.assertIsNotNone(active_customer)

    def test_create_payment_option(self):
        save_customer_to_database(self.first_name,self.last_name,self.phone_number,self.address)
        customer_id = get_customer(self.first_name,self.last_name,self.phone_number, self.address)

        self.assertIsNotNone(customer_id)

        select_active_customer(2)

        self.assertIsNotNone(active_customer)

        save_payment_option_to_database(self.payment_type,self.account_number, active_customer)

        payment_id = get_payment_option(self.payment_type,self.account_number active_customer)

        self.assertIsNotNone(payment_id)


if __name__ == '__main__':
    unittest.main()
