given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
index1 = 8
if index1 <= len(given_list) - 1:
    given_list.remove(given_list[index1])
    print("List after removing element at index", index1, "is", given_list)
else:
    print("Index out of range")