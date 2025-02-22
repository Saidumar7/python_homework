# 1
def convert_cel_to_far(celsius):
    """Converts Celsius to Fahrenheit."""
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5/9, 2)

fahrenheit = float(input("Enter a temperature in degrees F: "))
celsius_result = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} degrees F = {celsius_result} degrees C\n")

celsius = float(input("Enter a temperature in degrees C: "))
fahrenheit_result = convert_cel_to_far(celsius)
print(f"{celsius} degrees C = {fahrenheit_result} degrees F")

# 2
def invest(amount, rate, years):
    """Calculates and displays investment growth over time."""
    for year in range(1, years + 1):
        amount += amount * rate  
        print(f"Year {year}: ${amount:.2f}")

principal = float(input("Enter the initial amount: "))
annual_rate = float(input("Enter the annual rate of return (as a percentage): ")) / 100  
num_years = int(input("Enter the number of years: "))

invest(principal, annual_rate, num_years)

# 3
factors = []
def find_factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

num = int(input("Enter a positive integer: "))

if num > 0:
    find_factors(num)
else:
    print("Please enter a positive integer.")

# 4
import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return students, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    return statistics.median(values)

students, tuitions = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuitions)
student_mean = mean(students)
student_median = median(students)
tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")  
print(f"Total tuition: $ {total_tuition:,}\n")

print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}\n")

print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")

# 5
def is_prime(n):
    if n < 2:
        return False  

    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False  

    return True  

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
