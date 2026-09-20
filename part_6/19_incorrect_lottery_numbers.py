# The file lottery_numbers.csv containts winning lottery numbers in the following format:

# Sample data
# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 
# inclusive.

# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may 
# not be present in the file, but errors in a similar format will be):

# The week number is incorrect:

# Sample data
# week zzc;1,5,13,22,24,25,26

# One or more numbers are not correct:

# Sample data
# week 22;1,**,5,6,13,2b,34

# Too few numbers:

# Sample data
# week 13;4,6,17,19,24,33

# The numbers are too small or large:

# Sample data
# week 39;5,9,15,35,39,41,105

# The same number appears twice:

# Sample data
# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file 
# should contain only those lines from the original file which are in the correct format.


## Solution:

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 
# inclusive.

def filter_incorrect():
    with open("lottery_numbers.csv") as lottery_file_info:
        with open('correct_numbers.csv', 'w') as correct_file_info:
            for data in lottery_file_info:
                line = data.replace("\n","")
                line = line.split(";")
                week = line[0].split(" ")
                lottery = line[1].split(",")

                # Case 1: The week number is incorrect:
                try:
                    week_number = int(week[1])
                except ValueError:
                    continue

                # Case 2: One or more numbers are not correct:
                try:
                    lottery = [int(num) for num in lottery[:]]
                except ValueError:
                    continue

                # Case 3: Too few numbers:
                if len(lottery) < 7 or len(lottery) > 7:
                    continue

                # Case 4: The numbers are too small or large:
                if False in [num in range(1, 40) for num in lottery]:
                    continue

                # Case 5: The same number appears twice:
                if len({num for num in lottery}) != 7:
                    continue

                with open('correct_numbers.csv', 'a') as correct_file_info:
                    correct_file_info.write(data)


if __name__ == "__main__":
    filter_incorrect()

