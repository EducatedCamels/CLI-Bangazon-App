import os
import sqlite3
import sys
sys.path.append('bangazon')
from CustomerManagement import *
from ProductManagement import *

active_customer = 1


class Bangazon():

    def build_menu(self):

        os.system('cls' if os.name == 'nt' else 'clear')
        print('*********************************************************')
        print('**  Welcome to Bangazon! Command Line Ordering System  **')
        print('*********************************************************\n')     
        print("1. Create Customer Account")
        print("2. Choose Active Customer")
        print("3. Create a Payment Option")
        print("4. Add Product to Shopping Cart")
        print("5. Complete an Order")
        print("6. See Product Popularity")

    
    def main_menu(self):

        self.build_menu()
        choice = input(">> ")

        if choice == "1":
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            phone_number = input("Phone Number: ")

            save_customer_to_database(first_name, last_name, address, phone_number)


        if choice == "2":

            customer_list = get_all_customers()
            for number, name in enumerate(customer_list):   
                print('{}. {}'.format(number+1, name[0]))

            customer_id = input("Select active customer")

            select_active_customer(customer_id)



        if choice == "3":
            payment_type = input("What is your payment type? ")
            account_number = input("What is your account number? ")

            save_payment_option_to_database(payment_type, account_number, active_customer)    



        if choice == "4":

            product_list = get_all_products()
            for number, product in enumerate(product_list):   
                print('{}. {}'.format(number+1, product[0]))

            product_id = input("Select product to add to cart")

            add_product_to_order(product_id)



        if choice == "5":

            get_active_order()

            selected_payment = input("Choose your payment type")

            select_payment_option(selected_payment)    

            complete_order()

            # print("Your order of '{}' is complete and your total is '{}'.")


        self.main_menu()



if __name__ == "__main__":
  bangazon = Bangazon()
  bangazon.main_menu()