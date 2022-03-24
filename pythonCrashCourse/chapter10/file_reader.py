filePath = 'pythonCrashCourse/chapter10/pi_digits.txt'

with open(filePath) as file_object:
    contents = file_object.read()
print(contents)
print("File content printed\n")

with open(filePath) as test_object:
    for line in test_object:
        print(line.rstrip())
        break
print("One line printed using for loop\n")

with open(filePath) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    print(line.rstrip())
    pi_string += line.strip()
print("Printing line by line\n")

with open(filePath) as file_object:
    lin = file_object.readline()
print(lin.rstrip())
print("Printing one line using readline()\n")

print(pi_string)
print("The string had", len(pi_string), "caracters length")
print("The whole string in one single line\n")


