import sys
import sqlite3
 
active_customer = None


def save_customer_to_database(first_name, last_name, address, phone_number):
	pass


def get_customer(first_name, last_name, address, phone_number):
	return 1


def get_all_customers():
	customer_list = [("Meg", "Dean", "Kayla")]
	return customer_list
		

def get_active_customer():
	return active_customer


def select_active_customer(customer_id):
	global active_customer
	active_customer = customer_id


def save_payment_option_to_database(payment_type, account_number, active_customer):

	with sqlite3.connect('bangazon.db') as connection:
		c = connection.cursor()

		c.execute("insert into payment values(?, ?, ?, ?)",
				(None, payment_type, account_number, active_customer))

		connection.commit()


def get_payment_option(payment_type, account_number, active_customer):
	return 2



