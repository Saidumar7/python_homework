given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = int(input("Enter an element to count: "))
count = 0
for i in given_list:
    if i == element:
        count += 1
print("Count of element", element, "is", count)