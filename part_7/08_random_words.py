# The exercise template contains the file words.txt, which contains some English language words, one on each line.

# Please write a function named words(n: int, beginning: str), which returns a list containing n random words from 
# the words.txt file. All words should begin with the string specified by the second argument.

# The same word should not appear twice in the list. If there are not enough words beginning with the specified 
# string, the function should raise a ValueError exception.

# An example of the function in action:

# word_list = words(3, "ca")
# for word in word_list:
#     print(word)
# Sample output
# cat
# car
# carbon


## Solution:

from random import sample

def words(n : int, beginning : str):
    with open("words.txt") as words_file :
        found_words = []
        for word in words_file:
            word = word.replace("\n", "")

            # if word.find(beginning, 0) == 0:  # whether the word begins with the string or not 
            if word.startswith(beginning):
                found_words.append(word)
            else:
                continue

            
            # if len(word) >= len(beginning):   ## Unnecessary looping to just find if the word begins with string ?
            #     found = ''
            #     for index in range(len(beginning)):
            #         if word[index] == beginning[index]:
            #             found = True
            #         else:
            #             found = False
            # if found == True:
            #     found_words.append(word)

        if len(found_words) >= n:
            return sample(found_words, k=n)
        else:
            raise ValueError


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)

