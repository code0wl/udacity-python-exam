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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

first_texter  = texts[0]
last_caller = calls[len(calls) - 1]

print(f"First record of texts, {first_texter[0]} texts {first_texter[1]} at time {first_texter[2]}" )
print(f"Last record of calls, {last_caller[0]} calls {last_caller[1]} at time {last_caller[2]}, lasting {last_caller[3]} seconds" )



