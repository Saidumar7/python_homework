given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in given_list:
    if i % 2 == 0:
        new_list.append(i)
print("New list with even elements is", new_list)