import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'root',
    'database': 'CLOTHRECORD',
}

def connect_to_database():
    try:
        mydatabase = mysql.connector.connect(**DB_CONFIG)
        return mydatabase
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

def display_records():
    mycursor = mydatabase.cursor()
    mycursor.execute("SELECT * FROM cloth")
    myresult = mycursor.fetchall()
    for cloth_id, Type, size, price in myresult:
        print(cloth_id, Type, size, price)
    mycursor.close()

def search_record():
    print("\nSEARCH CLOTH BY ITS ID")
    r1 = input("ENTER CLOTH_ID: ")
    mycursor = mydatabase.cursor()
    mycursor.execute("SELECT * FROM cloth WHERE cloth_id=%s", (r1,))
    myresult = mycursor.fetchall()
    for cloth_id, Type, size, price in myresult:
        print(cloth_id, Type, size, price)
    mycursor.close()

def delete_record():
    print("\nDELETE CLOTH RECORD")
    r1 = input("ENTER CLOTH ITEM ID TO DELETE: ")
    mycursor = mydatabase.cursor()
    mycursor.execute("DELETE FROM cloth WHERE cloth_id=%s", (r1,))
    mydatabase.commit()
    print("Record deleted successfully!")
    mycursor.close()

def update_record():
    r1 = input("ENTER CLOTH ID WHOSE PRICE YOU WANT TO UPDATE: ")
    newprice = input("ENTER NEW PRICE: ")
    mycursor = mydatabase.cursor()
    mycursor.execute("UPDATE cloth SET price=%s WHERE cloth_id=%s", (newprice, r1))
    mydatabase.commit()
    mycursor.execute("SELECT * FROM cloth WHERE cloth_id=%s", (r1,))
    myresult = mycursor.fetchall()
    for cloth_id, Type, size, price in myresult:
        print(cloth_id, Type, size, price)
    mycursor.close()

def add_record():
    print("\n*ENTER CLOTH DETAILS*")
    c = input("ENTER CLOTH_ID: ")
    l = input("ENTER TYPE: ")
    o = input("ENTER SIZE: ")
    t = input("ENTER PRICE: ")
    mycursor = mydatabase.cursor()
    sql_insert = "INSERT INTO cloth (cloth_id, Type, size, price) VALUES (%s, %s, %s, %s)"
    values_insert = (c, l, o, t)
    mycursor.execute(sql_insert, values_insert)
    mydatabase.commit()
    print("Information Saved")
    mycursor.close()

def view_by_type():
    mycursor = mydatabase.cursor()
    cloth_type = input("Enter cloth type to view: ")
    mycursor.execute("SELECT * FROM cloth WHERE Type=%s", (cloth_type,))
    myresult = mycursor.fetchall()
    for cloth_id, Type, size, price in myresult:
        print(cloth_id, Type, size, price)
    mycursor.close()

def view_by_size():
    mycursor = mydatabase.cursor()
    cloth_size = input("Enter cloth size to view: ")
    mycursor.execute("SELECT * FROM cloth WHERE size=%s", (cloth_size,))
    myresult = mycursor.fetchall()
    for cloth_id, Type, size, price in myresult:
        print(cloth_id, Type, size, price)
    mycursor.close()

def calculate_total_price():
    mycursor = mydatabase.cursor()
    mycursor.execute("SELECT SUM(price) FROM cloth")
    total_price = mycursor.fetchone()[0]
    print(f"Total Price of all cloth items: {total_price}")
    mycursor.close()

def sort_records():
    mycursor = mydatabase.cursor()
    sort_option = input("Enter sort option (cloth_id, Type, size, price): ")
    mycursor.execute(f"SELECT * FROM cloth ORDER BY {sort_option}")
    myresult = mycursor.fetchall()
    for cloth_id, Type, size, price in myresult:
        print(cloth_id, Type, size, price)
    mycursor.close()

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main_menu():
    while True:
        print("\nMAIN MENU")
        print("_")
        print("1. ADD RECORD")
        print("2. DISPLAY RECORD")
        print("3. SEARCH RECORD")
        print("4. DELETE RECORD")
        print("5. UPDATE RECORD")
        print("6. VIEW BY TYPE")
        print("7. VIEW BY SIZE")
        print("8. CALCULATE TOTAL PRICE")
        print("9. SORT RECORDS")
        print("10. EXIT")
        print("_")
        choice = get_int_input("ENTER YOUR CHOICE: ")

        if choice == 1:
            add_record()
        elif choice == 2:
            display_records()
        elif choice == 3:
            search_record()
        elif choice == 4:
            delete_record()
        elif choice == 5:
            update_record()
        elif choice == 6:
            view_by_type()
        elif choice == 7:
            view_by_size()
        elif choice == 8:
            calculate_total_price()
        elif choice == 9:
            sort_records()
        else:
            break

# Main program starts here
mydatabase = connect_to_database()

while True:
    print("\nLOGIN")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "computer" and password == "12":
        print("Login successful")
        main_menu()
    else:
        print("\nInvalid username and password!")
        break

mydatabase.close()
