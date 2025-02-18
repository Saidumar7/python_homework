given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10]
element1 = 5
first_occurrence = given_list.index(element1)
given_list.remove(element1)
element2 = 19
given_list.insert(first_occurrence, element2)
print("List after removing element", element1, "and inserting element", element2, "at index", first_occurrence, ":", given_list)