import os

FILE_NAME = "bank_data.txt"


def create_account():
    name = input("Enter your name: ")
    balance = 0

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{balance}\n")

    print("✅ Account created successfully!")


def view_accounts():
    if not os.path.exists(FILE_NAME):
        print("❌ No accounts found")
        return

    print("\n📋 Account List:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, balance = line.strip().split(",")
            print(f"Name: {name} | Balance: ₹{balance}")


def deposit():
    name = input("Enter account name: ")
    amount = float(input("Enter amount to deposit: "))

    updated = False
    new_data = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            acc_name, balance = line.strip().split(",")
            balance = float(balance)

            if acc_name == name:
                balance += amount
                updated = True

            new_data.append(f"{acc_name},{balance}")

    with open(FILE_NAME, "w") as file:
        for line in new_data:
            file.write(line + "\n")

    if updated:
        print("💰 Amount deposited!")
    else:
        print("❌ Account not found")


def withdraw():
    name = input("Enter account name: ")
    amount = float(input("Enter amount to withdraw: "))

    updated = False
    new_data = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            acc_name, balance = line.strip().split(",")
            balance = float(balance)

            if acc_name == name:
                if balance >= amount:
                    balance -= amount
                    print("💸 Withdrawal successful")
                else:
                    print("❌ Insufficient balance")
                updated = True

            new_data.append(f"{acc_name},{balance}")

    with open(FILE_NAME, "w") as file:
        for line in new_data:
            file.write(line + "\n")

    if not updated:
        print("❌ Account not found")


def menu():
    print("\n🏦 BANK SYSTEM")
    print("1. Create Account")
    print("2. View Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        view_accounts()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        print("👋 Thank you!")
        break
    else:
        print("❌ Invalid choice")