# Manually closing a file
file_object = open("myfile", 'r')
line = file_object.readline()
# . . . Any further processing of the file goes here . . .
file_object.close()

# Automatically closing a file
with open("myfile", 'r') as file_object:
    line = file_object.readline()
    # . . . Any further processing of the file goes here . . .

