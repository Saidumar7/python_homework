given_list = [1, 2, 4, 3, 2, 6, 8, 5, 3, 2, 9, 1]
unique_original_order = []
for i in given_list:
    if i not in unique_original_order:
        unique_original_order.append(i)
print("Unique elements in the original order are", unique_original_order)