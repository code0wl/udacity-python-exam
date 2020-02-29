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

callers = {}

for call in calls:
    call_duration = float(call[3])
    callers[call[0]] = call_duration
    callers[call[1]] = call_duration

longest_call = max(zip(callers.values(), callers.keys()))

print(
    f"{longest_call[1]} spent the longest time, {longest_call[0]} seconds, on the phone during September 2016.")
