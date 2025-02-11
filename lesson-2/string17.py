input_string = input("Enter a string: ")
vovels = "aeiou"
for char in input_string:
    if char in vovels:
        input_string = input_string.replace(char, "*")
print(input_string)