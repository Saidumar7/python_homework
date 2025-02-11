user_input = input("Enter a string: ")
vovels = "aeiou"
count = 0
for char in user_input:
    if char.lower() in vovels:
        count += 1
print("The string contains", count, "vovels.")
count = 0
for char in user_input:
    if char.lower() not in vovels:
        count += 1
print("The string contains", count, "consonants.")
