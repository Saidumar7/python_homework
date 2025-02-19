import random
lst = []
for i in range(1, 5):
    a = random.randint(1, 10)
    lst.append(a)
set_1 = set(lst)
print("Set that contains random elements from 1 to 10 is", set_1)