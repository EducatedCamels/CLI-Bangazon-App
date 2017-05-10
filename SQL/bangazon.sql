	create table Product (
		ProductID integer not null primary key autoincrement,
		price integer not null,
		title text not null
	
	)
	create table Payment(
		PaymentID integer not null primary key autoincrement,
		payment_type text not null,
		account_number integer not null ,
		CustomerID integer not null,
		foreign key (CustomerID) references Customer(CustomerID)
	)
	create table ProductOrder(
		ProductOrderID integer not null primary key autoincrement,
		ProductID integer not null,
		OrderID integer not null,
		foreign key (ProductID) references Product(ProductID),
		foreign key (OrderID) references `Order`(OrderID)
	)
	
	create table `Order` (
		OrderID integer not null primary key autoincrement,
		CustomerID integer not null,
		PaymentID integer not null,
		foreign key (CustomerID) references Customer(CustomerID),
		foreign key (PaymentID) references Payment(PaymentID)
	)

	create table Customer (
		CustomerID integer not null primary key autoincrement,
		first_name text not null,
		last_name text not null,
		address text not null,
		phone_number integer not null	
	)