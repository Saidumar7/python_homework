given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
given_list1 = given_list[::]
max_value = max(given_list)

while max_value in given_list1:
    given_list1.remove(max_value)
        
max_value2 = max(given_list1)
print("Second largest number in the list is", max_value2)