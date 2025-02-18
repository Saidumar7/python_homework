import random

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []

i = 5 # number of elements to be added to the new list
while i > 0:
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    if a > b:
        a, b = b, a
    new_list.append(given_list[a:b])
    i -= 1

print("New list with random elements is", new_list)
