given_list = [1, 3, 3, 2, 6, 4, 6, 7, 3, 10, 4, 3]
given_list1 = given_list.copy()
element = 3
indices = []
for i in given_list:
    if i == element:
        indices.append(given_list1.index(i))
        given_list1[given_list1.index(i)] = None
print("Indices of element", element, "in the list are", indices)