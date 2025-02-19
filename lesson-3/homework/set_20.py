set_1 = {2, 4, 6}
set_2 = {7, 8, 9}
def disjoint(set_1, set_2):
    return set_1.isdisjoint(set_2)
if disjoint(set_1, set_2):
    print("set_1 and set_2 are disjoint")
else:
    print("set_1 and set_2 are not disjoint")