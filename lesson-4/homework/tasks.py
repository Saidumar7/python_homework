# 1
list1 = list(map(int, input("Enter space seperated elements of the first list: ").split()))
list2 = list(map(int, input("Enter space seperated elements of the second list: ").split()))
for i in list1:
    if i in list2:
        c1 = list1.count(i)
        c2 = list2.count(i)
        for j in range(c1):
            list1[list1.index(i)] = None
        for k in range(c2):
            list2[list2.index(i)] = None

uncommon_elements = []
for w in (list1+list2):
    if w != None:
        uncommon_elements.append(w)
print(uncommon_elements)

# 2
n = int(input("Enter n: "))
for i in range(1,n):
    print(i**2)

# 3
txt = input("Enter the text: ")
vowels = {'a', 'o', 'e', 'u', 'i'}
result = []
count = 0

i = 0
while i < len(txt):
    result.append(txt[i])  
    count += 1

    if count == 3:
        if (i + 1 < len(txt)) and (txt[i] not in vowels):  
            result.append("_")
            count = 0  
        else:
            count -= 1  
    i += 1

print("".join(result))

# 4
import random

def play_game():
    number = random.randint(1, 100)  
    attempts = 10  

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/{attempts}: Enter your guess → ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it right!")
            return  
        
    print("You lost. Want to play again?")
    retry = input("Type 'Y', 'YES', 'y', 'yes', or 'ok' to restart: ").strip().lower()
    if retry in ['y', 'yes', 'ok']:
        play_game()  

play_game()

# 5
def check_password():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password is too short.")
        return

    if not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
        return

    print("Password is strong.")

check_password()

# 6
print("Prime numbers between 1 and 100:")

for num in range(2, 101):  
    is_prime = True  

    for divisor in range(2, int(num ** 0.5) + 1):  
        if num % divisor == 0:
            is_prime = False  
            break  

    if is_prime:
        print(num, end=" ") 


