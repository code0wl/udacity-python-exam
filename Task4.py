"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

bangalor_telemarketeer_numbers = []
bangalor_telemarketeer_rules = ['140']

def addNumber(number, rule):
  if re.search(f"^{rule}", number) and number not in bangalor_telemarketeer_numbers:
    bangalor_telemarketeer_numbers.append(number)


for call in calls: 
  number_one = call[0]
  number_two = call[1]
  
  for rule in bangalor_telemarketeer_rules:
    addNumber(number_one, rule)
    addNumber(number_two, rule)


print(rf"These numbers could be telemarketers:" + '\n'.join([ str(num) for num in bangalor_telemarketeer_numbers ]))
