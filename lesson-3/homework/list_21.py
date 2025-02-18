given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10]
given_list1 = given_list.copy()
min_value = min(given_list)
while min_value in given_list1:
    given_list1.remove(min_value)
min_value2 = min(given_list1)
print("Second smallest number in the list is", min_value2)