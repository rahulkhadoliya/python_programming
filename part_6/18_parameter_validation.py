# Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the 
# data in the arguments. The first element should be the name and the second the age.

# If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

# Invalid parameters in this case include:

# name is an empty string
# name contains less than two words
# name is longer than 40 characters
# age is a negative number
# age is greater than 150


## Solution:


def new_person(name: str, age: int):
    if name == "":
        raise ValueError("name is an empty string")

    name_list = name.split(" ")
    if len(name_list) == 1:
        raise ValueError("name contains less than two words")

    if len(name) > 40:
        raise ValueError("name is longer than 40 characters")

    if age < 0:
        raise ValueError("age is a negative number")

    if age > 150:
        raise ValueError("age is greater than 150")

    else:
        return (name, age)