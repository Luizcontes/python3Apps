import json

numbers = [1, 2, 3, 4]

filename = 'pythonCrashCourse/chapter10/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)