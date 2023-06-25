with open ('files-folder/myfile.txt', 'r') as file_object:
    line = file_object.readline()
    print(line)

import os 
file_name = os.path.join('files-folder', 'myfile.txt')
print(file_name)
file_object = open(file_name, 'r')