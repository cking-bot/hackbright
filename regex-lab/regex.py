import re

date_validation = re.compile(r'(\d{2})/(\d{2})/(\d{4})')

print("enter a date in this format: mm/dd/yyyy")
date_string = input()

match = date_validation.match(date_string)