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

non_tele = set()
outgoing = set()

for call in calls: 
  number_one = call[0]
  number_two = call[1]

  outgoing.add(number_one)
  non_tele.add(number_two)

for text in texts: 
  number_one = text[0]
  number_two = text[1]

  non_tele.update([number_one ,number_two])

possible_tele = outgoing.symmetric_difference(non_tele)

print(rf"These numbers could be telemarketers:" + '\n'.join([ str(num) for num in possible_tele ]))
