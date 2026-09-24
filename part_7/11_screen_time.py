# Please write a program for recording the amount of time the user has spent in front of a television, computer or 
# mobile device screen over a specific period of time.

# The program should work as follows:

# Sample output
# Filename: late_june.txt
# Starting date: 24.6.2020
# How many days: 5
# Please type in screen time in minutes on each day (TV computer mobile):
# Screen time 24.06.2020: 60 120 0
# Screen time 25.06.2020: 0 0 0
# Screen time 26.06.2020: 180 0 0
# Screen time 27.06.2020: 25 240 15
# Screen time 28.06.2020: 45 90 5
# Data stored in file late_june.txt

# The user will input each day on a separate line, and the entries will contain three numbers separated by spaces, 
# representing minutes.

# With the above input, the program should store the data in a file named late_june.txt. The contents should look 
# like this:

# Sample data
# Time period: 24.06.2020-28.06.2020
# Total minutes: 780
# Average minutes: 156.0
# 24.06.2020: 60/120/0
# 25.06.2020: 0/0/0
# 26.06.2020: 180/0/0
# 27.06.2020: 25/240/15
# 28.06.2020: 45/90/5


## Solution:

from datetime import timedelta,date

def add_days(current_date : str, add_days : int):
    try:
        current_date = current_date.split(".")

        Date = int(current_date[0])
        month = int(current_date[1])
        year = int(current_date[2])

        present_date = date(year, month, Date)
        new_date = present_date + timedelta(days= add_days)

        return "{:02d}.{:02d}.{:04d}".format(new_date.day, new_date.month, new_date.year)
        # return f"{new_date.day}.{new_date.month}.{new_date.year}"
    except (ValueError, IndexError):
        return "Invalid date format"


file_name = input("Filename: ")
start_date = input("Starting date: ")
no_of_days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile):")

date_dict = {}
for days in range(0, no_of_days):
    current_date = add_days(start_date, days)
    date_dict[current_date] = input(f"Screen time {current_date}: ") 



total_min = 0
for key, value in date_dict.items():
    value = [int(num) for num in value.split()]
    total_min += sum(value)

with open(file_name, 'w') as date_file:
    date_file.write(f"Time period: {add_days(start_date, 0)}-{add_days(start_date, no_of_days - 1)}\n")
    date_file.write(f"Total minutes: {total_min}\n")
    date_file.write(f"Average minutes: {total_min / no_of_days}\n")
    for key, value in date_dict.items():
        date_file.write(f"{key}: {value.replace(" ", "/")}\n")
    print("Data stored in file late_june.txt")

