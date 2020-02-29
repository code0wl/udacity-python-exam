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


def bangalore_area_code(number):
    return re.match(r'^\(080\)', number)


def has_area_code(number):
    return re.match(r'^\(.*\)', number)


def has_mobile_prefix(number):
    return re.match(r'^\d{4}', number)


def filter_area_code(number):
    code = has_area_code(number) or has_mobile_prefix(number)
    return code[0]


def incoming_calls(calls):
    numbers_called = set()
    domestic_calls = 0
    incoming_calls = 0

    for call in calls:
        caller = call[0]
        receiver = call[1]
        if bangalore_area_code(caller):
            domestic_calls += 1
            numbers_called.add(receiver)

            if bangalore_area_code(receiver):
                incoming_calls += 1

    percent_within_bangalore = incoming_calls / domestic_calls

    return numbers_called, percent_within_bangalore


def answer():
    print("The numbers called by people in Bangalore have codes:")
    codes = set()
    list_of_calls, percent = incoming_calls(calls)

    for number in sorted(list_of_calls):
        area_code = filter_area_code(number)
        if area_code not in codes:
            codes.add(area_code)
            print(area_code)

    percentage = round(percent * 100, 2)

    print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


answer()
