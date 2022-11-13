CREATE DATABASE billing_app;
USE billing_app;
CREATE TABLE main_bill(bill_no int, customer_name varchar(25), phone_no varchar(15), total varchar(10), biller_name varchar(15), PRIMARY KEY (bill_no));
