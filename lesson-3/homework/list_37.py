given_list = [2, -4, 5, -6, 7, -8, 9, -10]
sum_negative = 0
for i in given_list:
    if i < 0:
        sum_negative += i
print("Sum of negative elements in the list is", sum_negative)