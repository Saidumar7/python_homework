# vector class
import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            raise TypeError("Unsupported operand type for multiplication.")

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)  
print(v1 + v2)  
print(v2 - v1) 
print(v1 * v2)  
print(3 * v1) 
print(v1.magnitude())  
print(v1.normalize())  

# Employee Records Manager Implementation
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    def __init__(self, file_path="employees.txt"):
        self.file_path = file_path

    def add_employee(self, employee):
        with open(self.file_path, "a") as file:
            file.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        try:
            with open(self.file_path, "r") as file:
                print("Employee Records:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No employee records found.")

    def search_employee(self, employee_id):
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    if line.startswith(str(employee_id)):
                        print("Employee Found:")
                        print(line.strip())
                        return
            print("Employee not found.")
        except FileNotFoundError:
            print("No employee records found.")

    def update_employee(self, employee_id, name=None, position=None, salary=None):
        updated_employees = []
        found = False
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    if line.startswith(str(employee_id)):
                        found = True
                        emp_data = line.strip().split(", ")
                        emp = Employee(emp_data[0], emp_data[1], emp_data[2], emp_data[3])
                        if name:
                            emp.name = name
                        if position:
                            emp.position = position
                        if salary:
                            emp.salary = salary
                        updated_employees.append(str(emp))
                    else:
                        updated_employees.append(line.strip())
            if not found:
                print("Employee not found.")
            else:
                with open(self.file_path, "w") as file:
                    for emp in updated_employees:
                        file.write(emp + "\n")
                print("Employee updated successfully!")
        except FileNotFoundError:
            print("No employee records found.")

    def delete_employee(self, employee_id):
        updated_employees = []
        found = False
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    if not line.startswith(str(employee_id)):
                        updated_employees.append(line.strip())
                    else:
                        found = True
            if not found:
                print("Employee not found.")
            else:
                with open(self.file_path, "w") as file:
                    for emp in updated_employees:
                        file.write(emp + "\n")
                print("Employee deleted successfully!")
        except FileNotFoundError:
            print("No employee records found.")

    def menu(self):
        while True:
            print("\nWelcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                employee = Employee(employee_id, name, position, salary)
                self.add_employee(employee)
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                self.search_employee(employee_id)
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                name = input("Enter new Name (leave blank to skip): ")
                position = input("Enter new Position (leave blank to skip): ")
                salary = input("Enter new Salary (leave blank to skip): ")
                self.update_employee(employee_id, name or None, position or None, salary or None)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


manager = EmployeeManager()
manager.menu()