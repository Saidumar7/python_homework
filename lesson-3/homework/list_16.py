given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in given_list:
    if i % 2 != 0:
        count += 1
print("Number of odd elements in the list is", count)