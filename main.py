import csv
from datetime import datetime
import os

def file_check():
    # Create users.csv if not exists
    if not os.path.exists("users.csv"):
        with open("users.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "password", "email"])

    # Create expense.csv if not exists
    if not os.path.exists("expense.csv"):
        with open("expense.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["username", "amount", "category", "date", "description"])


# -----signup -----
def signup():
    username=input("Enter Username:")
    password=input("Enter Password:")
    email=input("Enter Email:")       

    with open("users.csv","r")as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) == 3 and row[2] == email:
                print("Email Already Exit")
                return

    with open("users.csv","a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow([username, password, email])
    print("Signup Successfully")
 

# ----------login for user----------

def login():
    attempts=3
    while attempts>0:
        username=input("Enter Username:")
        password=input("Enter password:")
        email=input("Enter email:")
        with open("users.csv","r")as file:
            reader=csv.reader(file)
            for row in reader:
                if len(row)==3:
                    if row[0]==username and row[1]==password and row[2]==email:
                        print("Login Successfully")
                        return username
        attempts-=1
        print("Try Again. Attempts left:".attempts)
    exit()


# ------- add expense -------
def add_expense(username):
    try:
        amount = float(input("Enter Amount:"))
    except:
        print("Invalid Amount")
        return

    category = input("Enter category(Food/Travel/Home Expenses):")
    description = input("Enter Description:")
    date = datetime.now().strftime("%Y-%m-%d")

    with open("expense.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, amount, category, date, description])

    print("Expense added successfully")



# ------- view expense -------
def view_expense(username):
    print("\n--- Your Expenses ---")

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) == 5 and row[0].strip() == username.strip():
                print(
                    "Amount:", row[1],
                    "| Category:", row[2],
                    "| Date:", row[3],
                    "| Description:", row[4]
                )

# ------- total expense -------
def total_expense(username):
    total = 0

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) == 5 and row[0].strip() == username.strip():
                total += float(row[1])

    print("Total Expense:", total)

# ------- delete expense -------
def delete_expense(username):

    expenses = []

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) == 5 and row[0].strip() == username.strip():
                expenses.append(row)

    
    if len(expenses) == 0:
        print("No expenses found")
        return

    
    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            "| Amount:", expense[1],
            "| Category:", expense[2],
            "| Date:", expense[3],
            "| Description:", expense[4]
        )

    
    try:
        choice = int(input("Enter expense number to delete: "))
    except:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid Expense Number")
        return

    
    delete_row = expenses[choice - 1]

    
    all_rows = []

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            all_rows.append(row)

    
    with open("expense.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for row in all_rows:
            if row != delete_row:
                writer.writerow(row)

    print("Expense Deleted Successfully")    

# ------- update expense -------
def update_expense(username):

    expenses = []

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) == 5 and row[0].strip() == username.strip():
                expenses.append(row)

    if len(expenses) == 0:
        print("No expenses found")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            i,
            "| Amount:", expense[1],
            "| Category:", expense[2],
            "| Date:", expense[3],
            "| Description:", expense[4]
        )

    try:
        choice = int(input("Enter expense number to update: "))
    except:
        print("Invalid Input")
        return

    if choice < 1 or choice > len(expenses):
        print("Invalid Expense Number")
        return

    selected = expenses[choice - 1]

    
    new_amount = input("Enter New Amount: ")
    new_category = input("Enter New Category: ")
    new_description = input("Enter New Description: ")

    
    all_rows = []

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            all_rows.append(row)

    
    with open("expense.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for row in all_rows:

            if row == selected:
                writer.writerow([
                    username,
                    new_amount,
                    new_category,
                    selected[3],
                    new_description
                ])
            else:
                writer.writerow(row)

    print("Expense Updated Successfully")

# ------- Monthly Report -------
def monthly_report(username):
    month = input("Enter Month (YYYY-MM): ")
    total = 0

    with open("expense.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == username and row[3].startswith(month):
                total += float(row[1])

    print("Monthly Expense:", total)


def main():
    file_check()

    print("\n==============================")
    print("     EXPENSE TRACKER SYSTEM")
    print("==============================")

    while True:
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            signup()

        elif choice == "2":
            username = login()
            if username is None:
                continue

            while True:
                print("\n1. Add Expense")
                print("2. View Expense")
                print("3. Total Expense")
                print("4. Delete Expense")
                print("5. Update Expense")
                print("6. Monthly Report")
                print("7. Logout")


                option = input("Enter option: ")

                if option == "1":
                    add_expense(username)

                elif option == "2":
                    view_expense(username)

                elif option == "3":
                    total_expense(username)

                elif option == "4":
                    delete_expense(username)

                elif option == "5":
                    update_expense(username)        

                elif option == "6":
                    monthly_report(username)

                elif option=="7":
                    break    

                else:
                    print("Invalid Option")

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid Choice")


main()



