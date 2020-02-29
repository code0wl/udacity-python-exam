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
    safe_numbers = set()
    for text in texts:
        safe_numbers.update([text[0], text[1]])
    for call in calls:
        safe_numbers.add(call[1])
    return safe_numbers


def tele(safe_numbers, calls):
    possible_spam = set()
    for info in calls:
        number = info[0]
        if number not in safe_numbers:
            possible_spam.add(number)
    return possible_spam


def answer():
    safe_numbers = non_tele(texts, calls)
    possible_spam = tele(safe_numbers, calls)
    sorted_nums = sorted(possible_spam)
    print("These numbers could be telemarketers: ", *sorted_nums, sep="\n")


answer()
