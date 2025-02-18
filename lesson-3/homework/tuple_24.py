given_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 1, 4, 2, 1)
def is_palindrome(given_tuple):
    return given_tuple == given_tuple[::-1]
if is_palindrome(given_tuple):  
    print("Tuple is palindrome")
else:
    print("Tuple is not palindrome")