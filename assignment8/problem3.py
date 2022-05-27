# Write a function which takes no input parameter and allow the user to enter words as many as the user wants until the user enters an empty word. When the user enters a word, the function will add the word to a list which was originally empty. Before the function adds the word to the list, it should check whether the same word had been already added to the list or not. If not, then the word is added to the list and if yes, the word should not be added to the list. The function will eventually return the list of words.
# o   Note: Only use List to solve this problem

list = []


def addListbyInput(word):
    count = 0
    while (len(word)):
        if len(list) != 0:
            for i in range(len(list)):
                if word == list[i]:
                    count = count + 1
                    print("This word has already inputed...")

            if count == 0:
                list.append(word)
        else:
            list.append(word)
        word = input("Let's input your favorite word : ")

    print('You inputed these word. %s' % list)


addListbyInput(input("Let's input your favorite word : "))
