# Exercise 5: Days of the Month - OPTIMIZED

days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

month = int(input("Enter the month number (1-12): "))

if month in days:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        print(f"February has {29 if leap == 'yes' else 28} days.")
    else:
        print(f"Month {month} has {days[month]} days.")
else:
    print("Invalid month. Enter 1-12.")