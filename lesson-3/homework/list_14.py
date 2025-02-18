given_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
def check_if_list_is_empty(given_list):
    if given_list:
        print("The list is not empty")
        return False
    else:
        print("The list is empty")
        return True
check_if_list_is_empty(given_list)