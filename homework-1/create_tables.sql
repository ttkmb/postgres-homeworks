-- SQL-команды для создания таблиц
create table employees
(
	employee_id int primary key,
	first_name varchar(25) not null,
	last_name varchar(25) not null,
	title varchar(100) not null,
	birth_date date,
	notes text
);

create table customers
(
	customer_id varchar(5) primary key,
	company_name text,
	contact_name varchar(100)
);

create table orders
(
	order_id int primary key,
	customer_id varchar(5) references customers(customer_id),
	employee_id int references employees(employee_id),
	order_date date,
	ship_city varchar(55)
)