filePath = 'pythonCrashCourse/chapter10/learningPython.txt'
with open(filePath) as file_object:
    file = file_object.read()
print(file)
print("***File read\n")

with open(filePath) as file_object:
    for line in file_object:
        print(line)
print("***File read line by line using for loop\n")

with open(filePath) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)
print("***File read as a list of lines\n")

for line in lines:
    print(line.replace("Python", "C"))
    