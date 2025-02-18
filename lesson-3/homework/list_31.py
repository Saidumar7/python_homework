given_list = [4, 3, 5, 2]
new_list = []
for i in given_list:
    j = i
    while j > 0:
        new_list.append(i)
        j -= 1
print("New list with repeated elements is", new_list)