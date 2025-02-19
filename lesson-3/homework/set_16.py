set_1 = {2, 4, 6, 3, 5}
set_2 = []
for i in set_1:
    if i % 2 == 0:
        set_2.append(i)       
set_2 = set(set_2)
print("Set after filtring evens",set_2)