# Please write an improved version of your password generator. The function now takes three arguments:

# If the second argument is True, the generated password should also contain one or more numbers.
# If the third argument is True, the generated password should also contain one or more of these special 
# characters: !?=+-()#.
# Despite these two additional arguments, the password should always contain at least one lowercase alphabet. 
# You may assume the function will only be called with combinations of arguments that are possible to formulate 
# into passwords following these rules. That is, the arguments will not specify e.g. a password of length 2 which 
# contains both a number and a special characters, for then there would not be space for the mandatory lowercase 
# letter.

# An example of how the function should work:

# for i in range(10):
#     print(generate_strong_password(8, True, True))
# Sample output
# 2?0n+u31
# u=m4nl94
# n#=i6r#(
# da9?zvm?
# 7h)!)g?!
# a=59x2n5
# (jr6n3b5
# 9n(4i+2!
# 32+qba#=
# n?b0a7ey


## Solution:

from random import choice, sample

def generate_strong_password(length : int, numerics : bool, specials : bool):
    possible_char = "qwertyuiopasdfghjklzxcvbnm"
    possible_numeric = '1234567890'
    possible_specials = '!?=+-()#'

    password = "" + choice(possible_char)
    for i in range(length - 1):
        if specials == True:
            if numerics == True:
                selection = choice([choice(possible_char), choice(possible_numeric), choice(possible_specials)])
            else:
                selection = choice([choice(possible_char), choice(possible_specials)])
        else:
            if numerics == True:
                selection = choice([choice(possible_char), choice(possible_numeric)])
            else:
                selection = choice(possible_char)

        password += selection

    return "".join(sample(password, k=length))

if __name__ == "__main__":
    print(generate_strong_password(5, True, True))
    print(generate_strong_password(5, True, True))
    print(generate_strong_password(5, True, False))
    print(generate_strong_password(5, True, False))
    print(generate_strong_password(5, True, False))