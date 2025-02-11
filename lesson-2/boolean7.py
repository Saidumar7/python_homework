first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
if (first_num+second_num) > 50.8:
    print("The sum of the numbers is greater than 50.8")
    if (10<first_num<=20) and (10<second_num<=20):
        print("The numbers are between 10 and 20.")
    else:
        print("The numbers are not between 10 and 20.")
else:
    print("The sum of the numbers is not greater than 50.8 , although the numbers are between 10 and 20.")