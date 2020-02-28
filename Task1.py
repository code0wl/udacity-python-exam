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

unique_phonenumbers = []


for call in calls:
    number1 = call[0]
    number2 = call[1]
    if number1 not in unique_phonenumbers:
        unique_phonenumbers.append(number1)        
    if number2 not in unique_phonenumbers:
        unique_phonenumbers.append(number2)

for text in texts:
    number1 = text[0]
    number2 = text[1]
    if number1 not in unique_phonenumbers:
        unique_phonenumbers.append(number1)        
    if number2 not in unique_phonenumbers:
        unique_phonenumbers.append(number2)

print(f"There are {len(unique_phonenumbers)} different telephone numbers in the records")

