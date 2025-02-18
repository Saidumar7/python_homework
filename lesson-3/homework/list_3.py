given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max = given_list[0]
for i in given_list:
    if i > max:
        max = i
print("Max element in the list is", max)