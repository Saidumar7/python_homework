# Zero Check Decorator
def check(func):
    def wrapper(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Nolga bo'lish mumkin emas"
    return wrapper

@check
def div(a, b):
   return a / b
print(div(6,2))

# Employee Records Manager
import os

FILE_NAME = "employees.txt"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            file.write("Employee ID, Name, Position, Salary\n")

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")
    
    with open(FILE_NAME, "a") as file:
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully!\n")

def view_employees():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            print("\nEmployee Records:")
            print(file.read())
    else:
        print("No employee records found.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("\nEmployee Found:")
                    print(line)
                    found = True
                    break
        if not found:
            print("Employee not found.\n")
    else:
        print("No employee records found.\n")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False
    lines = []
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        
        with open(FILE_NAME, "w") as file:
            for line in lines:
                if line.startswith(emp_id + ","):
                    print("\nCurrent Employee Details:")
                    print(line)
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    updated = True
                    print("Employee record updated successfully!\n")
                else:
                    file.write(line)
        
        if not updated:
            print("Employee not found.\n")
    else:
        print("No employee records found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False
    lines = []
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
        
        with open(FILE_NAME, "w") as file:
            for line in lines:
                if not line.startswith(emp_id + ","):
                    file.write(line)
                else:
                    deleted = True
            if deleted:
                print("Employee record deleted successfully!\n")
            else:
                print("Employee not found.\n")
    else:
        print("No employee records found.\n")

def main_menu():
    while True:
        print("Employee Records Manager")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
if __name__ == "__main__":
    create_file()
    main_menu()

# Word Frequency Counter
import os
import string
from collections import Counter

INPUT_FILE = "sample.txt"
OUTPUT_FILE = "word_count_report.txt"

def create_sample_file():
    if not os.path.exists(INPUT_FILE):
        print(f"'{INPUT_FILE}' does not exist. Please enter some text to create it.")
        user_input = input("Type a paragraph or text: ")
        with open(INPUT_FILE, "w") as file:
            file.write(user_input)
        print(f"'{INPUT_FILE}' has been created.\n")

def clean_and_split_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

def count_word_frequency(words):
    return Counter(words)

def generate_report(word_counts, total_words):
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in word_counts.most_common(5):
        print(f"{word} - {count} times")

    with open(OUTPUT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in word_counts.most_common(5):
            file.write(f"{word} - {count}\n")
    print(f"\nReport saved to '{OUTPUT_FILE}'.")

def main():
    create_sample_file()

    with open(INPUT_FILE, "r") as file:
        text = file.read()

    words = clean_and_split_text(text)

    word_counts = count_word_frequency(words)

    total_words = len(words)

    generate_report(word_counts, total_words)

if __name__ == "__main__":
    main()