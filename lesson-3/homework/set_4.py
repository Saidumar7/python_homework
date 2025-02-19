set_1 = {2, 4, 6}
set_2 = {4, 6, 7, 2}
def is_subset(set_1, set_2):
    return set_1.issubset(set_2)
if is_subset(set_1, set_2):
    print("set_1 is subset of set_2")
else:
    print("set_1 is not subset of set_2")