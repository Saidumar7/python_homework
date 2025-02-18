given_tuple = (2, 3, 4, 5, 6, 8, 9, 10, 1, 3, 1, 4, 2)
def nested_subtuples(given_tuple):
    i=len(given_tuple)
    lst=[]
    while i>2:
        lst.append(given_tuple[i-2:i])
        i-=2
        if i<2:
            lst.append(given_tuple[i-1])
            break
    lst.reverse()
    return tuple(lst)
print("Nested sub-tuples are", nested_subtuples(given_tuple))