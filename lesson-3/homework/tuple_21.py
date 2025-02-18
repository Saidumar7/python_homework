given_tuple = (1, 2, 5)
lst=[]
def repetead_tuple(given_tuple):
    for j in given_tuple:
        i= j
        while i>0:
            lst.append(j)
            i-=1
    return tuple(lst)
print("Repeated tuple is", repetead_tuple(given_tuple))