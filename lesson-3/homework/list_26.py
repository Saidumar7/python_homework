given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def middle_elements(given_list):
    if len(given_list) % 2 == 0:
        middle_elements = given_list[int(len(given_list)/2)-1:int(len(given_list)/2)+1]
    else:
        middle_elements = given_list[int(len(given_list)/2)]
    return middle_elements
print("Middle element(s) in the list: ", middle_elements(given_list))