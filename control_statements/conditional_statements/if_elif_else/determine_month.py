# Program to determine the season based on the month

month = int(input("Enter the month number (1-12): "))

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")

