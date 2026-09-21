# The Python module string contains some string constants, which define certain groups of characters. These 
# include for example lowercase letters and punctuation characters. Please familiarize yourself with these 
# constants, and then write a function named separate_characters(my_string: str). The function takes a string as 
# its argument, and it should separate the characters in the string into three other strings, and return these in 
# a tuple:

# The first string should contain the lowercase and uppercase ASCII letters (string constant ascii_letters)
# The second string should contain all punctuation characters defined by the string constant punctuation
# The third string should contain all the other characters (including whitespace)
# The characters should appear in the three strings in the same order as they appeared in the original string.

# An example of the function in action:

# parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(parts[0])
# print(parts[1])
# print(parts[2])
# Sample output
# OlHeyaremltswrking
# !!!,?
# é  üäü ö


## Solution: 

import string

## Here for our question we will need four functions from string module 
## i.e. ascii_uppercase, ascii_lowercase, punctuation, printable
## these functions give ascii alphabet string only not filter them. 
## we can use it to check whether the current char is of ascii alphabet 

def separate_characters(my_string : str):
    # simple use of for loop
    # for char in my_string:
    #     if char in string.ascii_uppercase:
    #         string_parts += char

    # Little bit complex bit easy representation
    upper_lower_string_parts = "".join([char for char in my_string if char in string.ascii_uppercase or char in string.ascii_lowercase])
    punctuation_string_parts = "".join([char for char in my_string if char in string.punctuation])
    ascii_string_parts = upper_lower_string_parts + punctuation_string_parts
    other_string_parts = "".join([char for char in my_string if char not in ascii_string_parts])

    return upper_lower_string_parts, punctuation_string_parts, other_string_parts

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])


