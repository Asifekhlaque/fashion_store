import mysql.connector
mydatabase=mysql.connector.connect(host="localhost",user="root",passwd="root")

#creating database and table
mycursor=mydatabase.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS CLOTHRECORD")
mycursor.execute("USE CLOTHRECORD")
mycursor.execute("CREATE TABLE IF NOT EXISTS CLOTH(cloth_id int,Type varchar(20),size varchar(3),price int)")

def success():
    while True:
        print("______________________________________________________________")
        print("***********************************MAIN MENU*****************************************")
        print("_______________________________________________________________________")
        print("1.ADD RECORD")
        print("2.DISPLAY RECORD")
        print("3.SEARCH RECORD")
        print("4.DELETE RECORD")
        print("5.UPDATE RECORD")
        print("6.EXIT")
        print("___________________________________________________________________")
        choice=int(input("ENTER YOUR CHOICE:"))

        if choice==1:
            print("____________________________________________________________________")
            print("************************************ENTER CLOTH DETAILS******************************************")
            print("______________________________________________________________________")
            c=input("ENTER CLOTH_ID:")
            l=input("ENTER TYPE:")
            o=input("ENTER SIZE:")
            t=input("ENTER PRICE:")
            mycursor=mydatabase.cursor()
            sql = "INSERT INTO cloth (cloth_id, Type, size, price) VALUES (%s, %s, %s, %s)"
            values = (c,l,o,t)
            mycursor.execute(sql, values)
            mydatabase.commit()
            print("\t\t\tInformation Saved")
            print("___________________________________________________________")

        elif choice == 2:
          mycursor = mydatabase.cursor()
          mycursor.execute("SELECT * FROM cloth")
          myresult = mycursor.fetchall()
          for cloth_id,Type, size, price in myresult:
            print(cloth_id,Type, size , price)
            
        elif choice == 3:
          print("__________________________________________________________")
          print("*************SEARCH CLOTH BY ITS ID*********")
          print("__________________________________________________________")
          r1 = input("ENTER CLOTH_ID")
          mycursor = mydatabase.cursor()
          mycursor.execute("SELECT * FROM cloth WHERE cloth_id=" + r1)
          myresult = mycursor.fetchall()
          for cloth_id, Type, size, price in myresult:
            print(cloth_id, Type, size, price)
          else:
            exit()
        elif choice == 4:
            print("__________________________________________________________")
            print("**********DELETE CLOTH RECORD*************")
            print("__________________________________________________________")
            r1 = input("ENTER CLOTH ITEM ID TO DELETE: ")
            mycursor = mydatabase.cursor()
            mycursor.execute("DELETE FROM cloth WHERE cloth_id=" + r1)
            mydatabase.commit()
            print("\t\t\tRecord deleted successfully!")
            print("________________________________________________________")
        elif choice == 5:
             r1 = input("ENTER CLOTH ID  WHOSE PRICE YOU WANT TO UPDATE")
             newprice = input("ENTER NEW PRICE")
             mycursor = mydatabase.cursor()
             mycursor.execute("UPDATE cloth SET price=" + newprice + " WHERE cloth_id=" + r1)
             mydatabase.commit()
             mycursor.execute("SELECT * FROM cloth WHERE cloth_id=" + str(r1))
             myresult = mycursor.fetchall()
             for cloth_id, Type, size, price in myresult:
                 print(cloth_id, Type, size, price)
        else:
             exit()

while True:
         print("____________________________________________________________")
         print("*************************LOGIN***************************")
         print("____________________________________________________________")

         username = input("Enter username: ")
         password = input("Enter password: ")
    
         if username == "computer" and password == "12":
             print("\t\t\tLogin successful")
             success()
         else:
            print("___________________________________________________________")
            print("\t\t\tInvalid username and password!")
            print("___________________________________________________________")
            break

    
