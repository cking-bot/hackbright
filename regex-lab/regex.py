import re

date_validation = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

print("Enter a date in this format: mm/dd/yyyy")
date_string = input()

match = date_validation.match(date_string)

if match:
    day, month, year = match.groups()
    day, month, year = int(day), int(month), int(year)

    print(day, month, year)

    if month < 1 or month > 12:
        print("date is invalid")

    elif year < 1900 or year > 2100:
        print("date is invalid")

    elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        print("date is invalid")

    elif month in [4, 6, 9, 11] and day > 30:
        print("date is invalid")

    elif month == 2:
        if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                print("date is invalid")
                
    else: 
        print("date is valid")
else: 
    print("date is invalid")

