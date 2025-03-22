import csv
import json

# Task 1: Library Management System
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member has reached the borrowing limit of 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, title):
        for book in self.books:
            if book.title == title:
                member.borrow_book(book)
                return
        raise BookNotFoundException("Book not found in the library.")

    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                member.return_book(book)
                return
        raise BookNotFoundException("Book was not borrowed by the member.")

# Task 2: Student Grades Management

def calculate_average_grades(input_file, output_file):
    subjects = {}
    counts = {}
    
    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['Subject']
            grade = int(row['Grade'])
            if subject not in subjects:
                subjects[subject] = 0
                counts[subject] = 0
            subjects[subject] += grade
            counts[subject] += 1
    
    averages = {subject: subjects[subject] / counts[subject] for subject in subjects}
    
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, round(avg, 2)])

# Task 3: JSON Handling

def load_tasks(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def save_tasks(json_file, tasks):
    with open(json_file, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

def task_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(task['completed'] for task in tasks)
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task['priority'] for task in tasks) / total_tasks if total_tasks else 0
    
    print(f"Total Tasks: {total_tasks}")
    print(f"Completed Tasks: {completed_tasks}")
    print(f"Pending Tasks: {pending_tasks}")
    print(f"Average Priority: {avg_priority:.2f}")

def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])

# Example Usage
if __name__ == "__main__":
    # Library System Test
    lib = Library()
    book1 = Book("1984", "George Orwell")
    book2 = Book("The Catcher in the Rye", "J.D. Salinger")
    lib.add_book(book1)
    lib.add_book(book2)
    
    member1 = Member("Alice")
    lib.add_member(member1)
    
    try:
        lib.borrow_book(member1, "1984")
        lib.borrow_book(member1, "The Catcher in the Rye")
        lib.borrow_book(member1, "Moby Dick")  # Should raise BookNotFoundException
    except Exception as e:
        print(e)
    
    # Grades Calculation Test
    calculate_average_grades("grades.csv", "average_grades.csv")
    
    # Task Management Test
    tasks = load_tasks("tasks.json")
    display_tasks(tasks)
    task_statistics(tasks)
    convert_json_to_csv("tasks.json", "tasks.csv")
