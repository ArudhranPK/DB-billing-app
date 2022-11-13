import mysql.connector

#authentication for the billing person
def authentication(username, password):
    try:
        global mysql_con
        mysql_con = mysql.connector.connect(host = "localhost", user = "arudhran", password = "arudhran", db = "billing_app")

        global mysql_cursor
        mysql_cursor = mysql_con.cursor()
        return True

    except:
        return False

def get_bill_no():
    mysql_cursor.execute("SELECT bill_no FROM main_bill")
    tmp_list = []

    for number in mysql_cursor.fetchall():
        tmp_list.append(number[0])

    return tmp_list

def get_main_bill():
    mysql_cursor.execute("SELECT * FROM main_bill")
    return mysql_cursor.fetchall()

def create_a_new_bill(bill_no, customer, phone, total, biller):
    mysql_cursor.execute(f"CREATE TABLE bill_{bill_no}(item_name varchar(35), price int, quantity int, total int)")
    mysql_con.commit()
    
    mysql_cursor.execute(f"INSERT INTO main_bill VALUES({bill_no}, '{customer}', '{phone}', '{total}', '{biller}')")
    mysql_con.commit()

def get_customer_bill(bill_no):
    mysql_cursor.execute(f"SELECT * FROM bill_{bill_no}")
    return mysql_cursor.fetchall()

def get_customer_name_and_phone_number(bill_no):
    mysql_cursor.execute(f"SELECT * FROM main_bill where bill_no = {bill_no}")
    return mysql_cursor.fetchall()[0]

def delete_customer_bill(bill_no):
    mysql_cursor.execute(f"DROP TABLE bill_{bill_no}")
    mysql_cursor.execute(f"DELETE FROM main_bill where bill_no = {bill_no}")
    mysql_con.commit()

def save_bill(bill_no, products, price, quantity, total, grand_total):

    for i in range(len(products)):
        mysql_cursor.execute(f"INSERT INTO bill_{bill_no} VALUES('{products[i]}', {price[i]}, {quantity[i]}, {total[i]})")
        mysql_con.commit()

    mysql_cursor.execute(f"UPDATE main_bill SET total = {grand_total} WHERE bill_no = {bill_no}")
    mysql_con.commit()
    
def delete_records(bill_no):
    mysql_cursor.execute(f"DELETE FROM bill_{bill_no}")
    mysql_con.commit()