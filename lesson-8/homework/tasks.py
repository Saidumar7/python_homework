# Farm
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} the {self.species} says {self.sound}!"

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name, "cow", "moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    def __init__(self, name):
        super().__init__(name, "chicken", "cluck")

    def lay_egg(self):
        return f"{self.name} laid an egg!"


class Sheep(Animal):
    def __init__(self, name):
        super().__init__(name, "sheep", "baa")

    def produce_wool(self):
        return f"{self.name} is producing wool."



cow = Cow("Sigrid")
chicken = Chicken("John")
sheep = Sheep("Sean")

print(cow.make_sound())  
print(chicken.eat("corn"))  
print(sheep.produce_wool())  
print(cow.sleep())  

# Bank Application

import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1  # Simple unique account number generation
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                self.save_to_file()
                print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
            else:
                print("Invalid deposit amount.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                self.save_to_file()
                print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")
        else:
            print("Account not found.")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            accounts_data = {acc_num: {"name": acc.name, "balance": acc.balance}
                            for acc_num, acc in self.accounts.items()}
            json.dump(accounts_data, file)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                accounts_data = json.load(file)
                for acc_num, data in accounts_data.items():
                    self.accounts[int(acc_num)] = Account(int(acc_num), data["name"], data["balance"])
        except FileNotFoundError:
            print("No existing accounts found. Starting fresh.")

    def menu(self):
        while True:
            print("\nWelcome to the Bank!")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter your name: ")
                initial_deposit = float(input("Enter initial deposit: "))
                self.create_account(name, initial_deposit)
            elif choice == "2":
                account_number = int(input("Enter account number: "))
                self.view_account(account_number)
            elif choice == "3":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                self.deposit(account_number, amount)
            elif choice == "4":
                account_number = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(account_number, amount)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


bank = Bank()
bank.menu()