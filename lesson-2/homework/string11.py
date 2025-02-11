user_input = input("Enter a string: ")
flag = False
for char in user_input:
    if char.isnumeric():
        print("The string has a number.")
        flag = True
        break
if not flag:    
    print("The string does not have a number.")
