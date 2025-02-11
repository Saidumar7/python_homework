print("Enter a word \'stop\' to stop the program.")
list_of_words = []
while True:
    word = input("Enter a word: ")
    if word == "stop":
        break
    else:   
        list_of_words.append(word)
for word in list_of_words:
    if list_of_words[-1] == word:
        print(word, end = ".")
    elif list_of_words[0] == word:
        print("The sentance seperated with \'-\':", word, end = "-")
    else:
        print(word, end = "-")
