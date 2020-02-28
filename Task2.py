"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_call = [0, 0, 0, 0]

for call in calls:
    call_duration = float(call[3])
    longest_call_duration = float(longest_call[3])
    if call_duration > longest_call_duration:
        longest_call = call


print(f"{longest_call[0]} spent the longest time, {longest_call[3]} seconds, on the phone during September 2016.")


