# The exercise template includes the file words.txt, which contains words in English.

# Please write a function named find_words(search_term: str). It should return a list containing all the words in 
# the file which match the search term.

# The search term may include lowercase letters and the following wildcard characters:

# -> A dot .means that any single character is acceptable in its place. For example, ca.would yield words like cat 
#   and car , p.ngwould yield words like ping and pong , and .a.ewould yield words like sane , care and late .
# -> An Asterisk *at the end of the search term means that any word which begins with the search term is acceptable. 
#   An Asterisk at the beginning of the search term means that any word which ends with the search term is acceptable. 
#   For example, ca*would yield words like california , cat , caring and Catapult , while *anewould yield words like 
#   crane , insane and airplane . There can only ever be a single Asterisk in the search term.
# -> If there are no wildcard characters in the search term, only words which match the search term exactly are 
#   returned.

# You may assume both wildcards are never used in the same search term.

# The words in the file are all written in lowercase. You may also assume the argument to the function will be in 
# lower case entirely.

# If no matching words are found, the function should return an empty list.

# Hint: the Pythons string methods startswith() and endswith() may be useful here. You can search for more 
# information about them online.

# An example of the function in action:

# print(find_words("*vokes"))
# Sample output
# ['convokes', 'equivokes', 'evokes', 'invokes', 'provokes', 'reinvokes', 'revokes']


## Solution:

# logic for the "." wild character : loop through the words and if 
#                                   word(i) == 'character' and all other sub character are true 
#                                   than save that word in the list

# logic foe the "*" wild character : use startswith() for "term*" case and endswith() for "*term"

def find_words(search_term: str):
    found_words_list = []
    with open('words.txt') as word_file_info:
        for word in word_file_info:
            word = word.replace("\n", "")

            if search_term[0] == "*":
                if word.endswith(search_term[1:]):
                    found_words_list.append(word)

            elif search_term[-1] == '*':
                if word.startswith(search_term[:-1]):
                    found_words_list.append(word)

            elif len(word) == len(search_term):
                for index in range(len(search_term)):
                    if search_term[index] == '.':
                        continue
                    elif search_term[index] != word[index]:
                        action = 'False'
                        break
                    else:
                        action = 'True'
                if action == 'True':
                    found_words_list.append(word)
    return found_words_list
                        
if __name__ == "__main__":
    print(find_words('c.r'))
    print(find_words('ca*'))
    print(find_words('*ane'))
    

                





