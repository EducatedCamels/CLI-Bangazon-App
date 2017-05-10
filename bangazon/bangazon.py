
class Bangazon()

	def build_menu(self):
	    os.system('cls' if os.name == 'nt' else 'clear')
	    print("1. Create Customer Account")
	    print("2. Choose Active Customer")
	    print("3. Create a Payment Option")
	    print("4. Add Product to Shopping Cart")
	    print("5. Complete an Order")
	    print("6. See Product Popularity")

	
	def main_menu(self):

		self.build_menu()
		choice = input(">> ")







		if choice == "3":
			payment_type = input("What is your payment type? ")
			account_number = input("What is your account number? ")

			save_payment_option_to_database(payment_type, account_number, active_customer)	








		if choice == "5":




			selected_payment = input()

			select_payment_option(selected_payment)	