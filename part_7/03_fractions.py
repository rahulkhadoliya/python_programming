# Please familiarize yourself with the Python module fractions. Use it to write a function named 
# fractionate(amount: int), which takes the number of parts as its argument. The function should divide the number 
# 1 into as many equal sized fractions as is specified by the argument, and return these in a list.

# An example of the function in action:

# for p in fractionate(3):
#     print(p)

# print()

# print(fractionate(5))
# Sample output
# 1/3
# 1/3
# 1/3

# [Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]


## Solution:

from fractions import Fraction

def fractionate(amount : int):
    fract_list = []
    for rep in range(0, amount):
        fract_list.append(Fraction(1, amount))
    return fract_list

if __name__ == "__main__":
    print(fractionate(5))
    for p in fractionate(3):
        print(p)
