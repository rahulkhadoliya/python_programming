# In this exercise you will validate Finnish Personal Identity Codes (PIC).

# Please write a function named is_it_valid(pic: str), which returns True or False based on whether the PIC given 
# as an argument is valid or not. Finnish PICs follow the format ddmmyyXyyyz, where ddmmyy contains the date of 
# birth, X is the marker for century, yyy is the personal identifier and z is a control character.

# The program should check the validity by these three criteria:

# The first half of the code is a valid, existing date in the format ddmmyy.
# The century marker is either + (1800s), - (1900s) or A (2000s).
# The control character is valid.
# The control character is calculated by taking the nine-digit number created by the date of birth and the personal 
# identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the 
# string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12, the control character would be C.

# More examples and explanations of the uses of the PIC are available at the Digital and Population Data Services 
# Agency.

# NB! Please make sure you do not share your own PIC, for example in the code you use for testing or through the 
# course support channels.

# Here are some valid PICs you can use for testing:

# 230827-906F
# 120488+246L
# 310823A9877


## Solution:

from datetime import datetime
from datetime import date as dt

def is_it_valid(pic : str):

    # case 1: The first half of the code is a valid, existing date in the format ddmmyy.
    if len(pic) > 11:
        return False
    try :
        date = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])

        if pic[6] == '+':
            year += 1800
        elif pic[6] == '-':
            year += 1900
        elif pic[6] == "A":
            year += 2000

        dt(year, month, date)
        
    except ValueError:
        return False

    # case 2: The century marker is either + (1800s), - (1900s) or A (2000s).
    try :
        if pic[6] == '+' or pic[6] == '-' or pic[6] == 'A':
            pass
    except ValueError:
        return False

    # case 3: The control character is valid.        
    key_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_value = int(f"{pic[0:6]}{pic[7:10]}")
    remainder = control_value % 31
    if key_string[remainder] == pic[10]:
        return True
    else :
        return False

if __name__ == "__main__":
    print(is_it_valid('080842-720N'))
    print(is_it_valid('230827-906F'))
    print(is_it_valid('230827-906F1'))


