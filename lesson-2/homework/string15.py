user_input = input("Enter a string: ")
accronym = ""
for word in user_input.split():
    accronym += word[0].upper()
print("The accronym of the string is", accronym)