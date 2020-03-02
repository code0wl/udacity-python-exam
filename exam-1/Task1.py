"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_phonenumbers = set()


for call in calls:
    unique_phonenumbers.update([call[0], call[1]])

for text in texts:
    unique_phonenumbers.update([text[0], text[1]])

print(
    f"There are {len(unique_phonenumbers)} different telephone numbers in the records")
