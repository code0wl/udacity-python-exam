"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
import decimal

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
bangalor_numbers = []
bangalor_rules = ['7', '8', '9', '140', r'\(080\)']

def addNumber(number, rule):
  if re.search(f"^{rule}", number) and number not in bangalor_numbers:
    bangalor_numbers.append(number)


for call in calls: 
  number_one = call[0]
  number_two = call[1]
  
  for rule in bangalor_rules:
    addNumber(number_one, rule)
    addNumber(number_two, rule)

bangalor_numbers.sort(key = str) 

print(rf"The numbers called by people in Bangalore have codes:" + '\n'.join([ str(num) for num in bangalor_numbers ]))


# Part B
domestic_landline_calls = []

for call in calls: 
  number_one = call[0]
  number_two = call[1]
  
  if re.match('^\(080\)', number_one) and re.match('^\(080\)', number_two):
    domestic_landline_calls.append(call)

percentage = round(len(calls) / len(domestic_landline_calls), 2)

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

