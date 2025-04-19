# DATABASE CONNNECTION

import mysql.connector
from tabulate import tabulate

# Connect to database
mydb = mysql.connector.connect(
    database="Students",
    host="127.0.0.1", #loclhost
    user="root",
    port=3306,
    password="12345",
)

def add_user():
    cursor = mydb.cursor()
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    email = input("Enter Email: ")

    sql = """
        INSERT INTO STD_Details (roll_no, name, Department, Email)
        VALUES (%s, %s, %s, %s)
    """
    val = (roll_no, name, dept, email)
    cursor.execute(sql, val)
    mydb.commit()
    print("✅ User added successfully.")

def update_user():
    cursor = mydb.cursor()
    roll_no = int(input("Enter Roll No to update: "))
    name = input("Enter New Name: ")
    dept = input("Enter New Department: ")
    email = input("Enter New Email: ")

    sql = """
        UPDATE STD_Details
        SET name = %s, Department = %s, Email = %s
        WHERE roll_no = %s
    """
    val = (name, dept, email, roll_no)
    cursor.execute(sql, val)
    mydb.commit()
    print("✅ User updated successfully.")

def delete_user():
    cursor = mydb.cursor()
    roll_no = int(input("Enter Roll No to delete: "))

    sql = "DELETE FROM STD_Details WHERE roll_no = %s"
    cursor.execute(sql, (roll_no,))
    mydb.commit()
    print("❌ User deleted successfully.")

def get_users():
    cursor = mydb.cursor()
    cursor.execute("SELECT roll_no, name, Department, Email FROM STD_Details")
    results = cursor.fetchall()

    headers = ["Roll No", "Name", "Department", "Email"]
    print("\n🎓 Student Details:\n")
    print(tabulate(results, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    while True:
        print("\n🧾 Menu:")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. Show All Users")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            update_user()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            get_users()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")
