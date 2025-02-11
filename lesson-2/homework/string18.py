user_input = input("Enter a string: ")
first_word = user_input.split()[0]
last_word = user_input.split()[-1]
if first_word == last_word:
    print("The first and last words are the same.")
else:
    print("Starts with:", first_word, "\nEnds with:", last_word)