# Please write a program which functions as a dictionary. The user can type in new entries or look for existing 
# entries.

# The program should work as follows:

# Sample output
# 1 - Add word, 2 - Search, 3 - Quit Function: 1 
# The word in Finnish: auto 
# The word in English: car 
# Dictionary entry added 1 - Add word, 2 - Search, 3 - Quit Function: 1 
# The word in Finnish: roska 
# The word in English: garbage 
# Dictionary entry added 1 - Add word, 2 - Search, 3 - Quit Function: 1 
# The word in Finnish: laukku 
# The word in English: bag 
# Dictionary entry added 1 - Add word, 2 - Search, 3 - Quit Function: 2 
# Search term: bag 
# roska - garbage laukku - bag 1 - Add word, 2 - Search, 3 - Quit Function: 2 
# Search term: car 
# auto - car 1 - Add word, 2 - Search, 3 - Quit Function: 2 
# Search term: laukku 
# laukku - bag 1 - Add word, 2 - Search, 3 - Quit Function: 3 
# Bye!

# The dictionary entries should be written to a file called dictionary.txt. The program should first read the 
# contents of the file. New entries are written to the end of the file whenever they are added to the dictionary.

# The format of the data stored in the dictionary is up to you.

# NB: the automatic tests for this exercise may change the contents of the file. If you want to keep its contents, 
# first make a copy of the file under a different name.

# NB2: this exercise doesn't ask you to write any functions, so you should n't place any code within an 
# if __name__ == "__main__"block.


## Solution:

# with open("dictionary.txt", 'w') as dictionary_file_info:
#     dictionary_file_info.write("dictionary = {}\n")

def update(finn_word : str, eng_word : str):
    # dictionary = {}  ## No need to create a dictionary here we can check the word directly line-by-line
    # line = f"dictionary[({finn_word}, {eng_word})] = " + f"{finn_word} - {eng_word}"
    with open("dictionary.txt", 'a') as dictionary_file_info:
        dictionary_file_info.write(f"{finn_word} - {eng_word} \n")

def search(word : str):
    with open("dictionary.txt") as dictionary_file_info:
        for line in dictionary_file_info:
            line = line.replace("\n", "")
            if word in line:
                print(line, end="")
            

while True:
    print("1 - Add word, 2 - Search, 3 - Quit ")
    action = input("Function: ")

    if action == '1':
        finnish_word = input("The word in Finnish: ")
        english_word = input("The word in English: ")
        update(finnish_word, english_word)
        print("Dictionary entry added ")
    elif action == '2':
        search_word = input("Search term: ")
        search(search_word)
    elif action == '3':
        print("Bye!")
        break
        

