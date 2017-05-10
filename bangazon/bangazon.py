
    if choice == "1":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        phone_number = input("Phone Number: ")

        save_customer_to_database(first_name, last_name, address, phone_number)
