given_list = [3, 4, 7, 2, 9, 10, 6, 8, 5]
def issorted(given_list):
    sorted_list = sorted(given_list)
    if given_list == sorted_list:
        return True
    else:
        return False
issorted(given_list)