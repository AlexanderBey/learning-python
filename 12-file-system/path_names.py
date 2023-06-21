import os 
print(os.path.join('bin','utils','disktools'))

path1 = os.path.join('mydir', 'bin')
path2 = os.path.join('utils', 'disktools', 'chdisk')

print(path1)
print(path2)
print('\n')
print('joined together')
print(os.path.join(path1, path2))


print('\n')
print('split the path')

path1 = os.path.join('some','path','to','split')
path_splitted = os.path.split(path1)

print(path1)
print(path_splitted)
print('\n')

print('base of the path')
path = os.path.join('some', 'directory','path.jpg')
print(path)
base_name = os.path.basename(path)
print(base_name)