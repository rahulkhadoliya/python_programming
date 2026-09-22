# Please write a function which creates passwords of a desired length, consisting of lowercase characters a to z.

# An example of how the function should work:

# for i in range(10):
#     print(generate_password(8))
# Sample output
# lttehepy
# olsxttjl
# cbjncrzo
# dwxqjdgu
# gpfdcecs
# jabyvgar
# xnbbonbl
# ktmsjyww
# ejhprmel
# rjkoacib


## Solution:

from random import choice

def generate_password(length : int):
    # possible_char = 'abcdefghijklmnopqrstuvwxyz' 
    possible_char = 'qwertyuiopasdfghjklzxcvbnm'  # since we already want randomness we can use the instid
    password = ''
    for i in range(length):
        password += choice(possible_char)
        
    # password = choices(possible_char, k = length) # retunrs a list elements of size k 
    return password


if __name__ == "__main__":

    print(generate_password(4))
    print(generate_password(4))
    print(generate_password(4))
    print(generate_password(4))


