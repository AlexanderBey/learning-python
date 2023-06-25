with open("files-folder/myfile.txt", 'w') as file_object:
    file_object.write("This is what i need to write in my file")

with open("files-folder/myfile.txt", 'r') as file_object:
    line = file_object.readline()
    print(line)
