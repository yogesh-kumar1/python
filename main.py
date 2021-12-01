import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="users")


def add():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    email = input("Enter Email: ")
    contact = input("Enter Number")

    res = conn.cursor()
    sql = "insert into user(name,age,email,contact) values(%s,%s,%s,%s)"
    res.execute(sql, (name, age, email, contact))
    conn.commit()
    print("\n")
    print("Added Successfully")

def view():
    res = conn.cursor()
    sql = "select * from user"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result,headers=["ID","NAME","AGE","EMAIL","CONTACT"]))

def update():
    print("1.Name: ")
    print("2.Age: ")
    print("3.Email: ")
    print("4.Contact: ")
    option = int(input("\nWhich field you need to update? : "))

    if option == 1:
        id = input("Enter your ID: ")
        name = input("Enter your Name: ")
        cu = conn.cursor()
        sql = "update user set name = %s where id = %s"
        cu.execute(sql,(name,id))
        conn.commit()
        view()
        print("\n")
        print("Updated Successfully")
    elif option ==2:
         id = input("Enter your ID: ")
         age = input("Enter your Age: ")
         cu = conn.cursor()
         sql = "update user set age = %s where id = %s"
         cu.execute(sql, (age, id))
         conn.commit()
         view()
         print("\n")
         print("Updated Successfully")
    elif option == 3:
         id = input("Enter your ID: ")
         email = input("Enter your Email: ")
         cu = conn.cursor()
         sql = "update user set email = %s where id = %s"
         cu.execute(sql, (email, id))
         conn.commit()
         view()
         print("\n")
         print("Updated Successfully")


    elif option == 4:
         id = input("Enter your ID: ")
         contact = input("Enter your Contact: ")
         cu = conn.cursor()
         sql = "update user set contact = %s where id = %s"
         cu.execute(sql, (contact, id))
         conn.commit()
         view()
         print("\n")
         print("Updated Successfully")
    else:
         print("Invalid")

def delete():

    id = input("Enter your ID: ")
    cu = conn.cursor()
    sql = "delete from user where id = %s"
    cu.execute(sql, (id,))
    conn.commit()
    print("\n")
    print("Deleted Successfully")






while True:
    print("\n")
    print("1.Add User ")
    print("2.View User ")
    print("3.Update User ")
    print("4.Delete User ")
    print("5.Exit ")
    print("\n")

    option = int(input("Enter Your Option : "))

    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        update()
    elif option == 4:
        delete()
    elif option == 5:
        quit()
    else:
        print("<<Invalid Input>>")





