import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'pythonCrashCourse/chapter10/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)