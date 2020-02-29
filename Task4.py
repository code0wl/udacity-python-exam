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


def non_tele(texts, calls):
    real_numbers = set()
    for text in texts:
        real_numbers.update([text[0], text[1]])
    for call in calls:
        real_numbers.add(call[1])
    return real_numbers


def telemarketers_set(real_numbers, calls):
    marketeers = set()
    for info in calls:
        number = info[0]
        if number not in real_numbers:
            marketeers.add(number)
    return marketeers


def answer():
    real_numbers = non_tele(texts, calls)
    marketeers = telemarketers_set(real_numbers, calls)
    print("These numbers could be telemarketers: ")
    for number in sorted(marketeers):
        print(number)


answer()
