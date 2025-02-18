given_list = [2, 4, 5, 9, 5, 4, 2]
def ispalindrome(given_list):
    reversed_list = given_list[::-1]
    if given_list == reversed_list:
        print("The list is a palindrome")
        return True
    else:
        print("The list is not a palindrome")
        return False
ispalindrome(given_list)
