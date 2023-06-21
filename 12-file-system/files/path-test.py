import os

path = 'C:\\Users\\alexa\\desktop\\dumbpython\\12-file-system\\files'

path_list = []

def print_path(path):
    # Appending text files paths to list
    for file in os.listdir(path):
        if file.endswith('.txt'):
            file_path = os.path.join(path, file)
            path_list.append(file_path)

    # Printing the list
    print('\n')
    print('-' * 50)
    print('Text file in directory')
    print('-' * 50)

    for path in path_list:
        print(path)
        print('\n')

print_path(path)

print('\n')
print('-' * 50)
print('Path testing')
print('-' * 50)

#file_path = os.path.join(path, 'one.txt')

print(path)

test1 = os.path.exists(path)
test2 = os.path.isfile(path)
test3 = os.path.isdir(path)


#print(test1)
#print(test2)
#print(test3)

with os.scandir(".") as my_dir:
    for entry in my_dir:
        print(entry.name, entry.is_file())

current_directory = os.getcwd()

print(current_directory)

