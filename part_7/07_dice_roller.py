# In this exercise you will write some functions which can be used in games that involve dice.

# Instead of normal dice this exercise specifies non-transitive dice. You can read up on these here or watch this 
# video.

# You will use three dice:

# Die A has the sides 3, 3, 3, 3, 3, 6
# Die B has the sides 2, 2, 2, 5, 5, 5
# Die C has the sides 1, 4, 4, 4, 4, 4
# Please write a function named roll(die: str), which rolls the die specified by the argument. An example of how 
# this should work:

# for i in range(20):
#     print(roll("A"), " ", end="")
# print()
# for i in range(20):
#     print(roll("B"), " ", end="")
# print()
# for i in range(20):
#     print(roll("C"), " ", end="")
# Sample output
# 3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  6  3  6  3
# 2  2  5  2  2  5  5  2  2  5  2  5  5  5  2  5  2  2  2  2
# 4  4  4  4  4  1  1  4  4  4  1  4  4  4  4  4  4  4  4  4

# Also write a function named play(die1: str, die2: str, times: int), which throws both dice as many times as 
# specified by the third argument. The function should return a tuple. The first item should be the number of 
# times die 1 won, the second the number of times die 2 won, and the third item should be the number of ties.

# result = play("A", "C", 1000)
# print(result)
# result = play("B", "B", 1000)
# print(result)
# Sample output
# (292, 708, 0)
# (249, 273, 478)


## Solution:

import random

def roll(die : str):
    die_A = 3, 3, 3, 3, 3, 6
    die_B = 2, 2, 2, 5, 5, 5
    die_C = 1, 4, 4, 4, 4, 4

    if die == 'A':
        return random.choice(die_A)
    elif die == 'B':
        return random.choice(die_B)
    elif die == 'C':
        return random.choice(die_C)

def play(die1: str, die2: str, times: int):
    # die_A = 3, 3, 3, 3, 3, 6
    # die_B = 2, 2, 2, 5, 5, 5
    # die_C = 1, 4, 4, 4, 4, 4

    times_die1_won = 0
    times_die2_won = 0
    ties = 0
    for i in range(times):
        die1_roll = roll(die1)
        die2_roll = roll(die2)
        if die1_roll > die2_roll:
            times_die1_won += 1
        elif die2_roll > die1_roll:
            times_die2_won += 1
        elif die1_roll == die2_roll:
            ties += 1
    return times_die1_won, times_die2_won, ties



if __name__ == "__main__":
    # for i in range(20):
    #     print(roll("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("C"), " ", end="")

    result = play("A", "B", 100)
    print(result)
    result = play("B", "B", 1000)
    print(result)