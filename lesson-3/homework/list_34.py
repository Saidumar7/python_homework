given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
given_list.insert(0, 0)
given_list[0] = given_list[-1]
given_list.pop()
print("List after shifting elements is", given_list)