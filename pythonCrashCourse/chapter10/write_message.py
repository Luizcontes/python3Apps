filename = 'pythonCrashCourse/chapter10/write_message.txt'

while 1:
    message = input("What would like to write to the file? ")
    
    if message == '0':
        break

    message += '\n'

    with open(filename, 'a') as file_object:
        file_object.write(message)
