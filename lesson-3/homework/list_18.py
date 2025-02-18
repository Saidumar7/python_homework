given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
given_list1 = given_list.copy()
sub_list = [4, 7]
flag = True
for i in sub_list:
    if i not in given_list1:
        flag = False
        break
    else:
        given_list1.remove(i)
        continue
if flag:
    print("Sublist is present in the given list")
else:
    print("Sublist is not present in the given list")