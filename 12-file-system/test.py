import os
print(os.getcwd())
print('\n')

print(os.listdir())
print(os.listdir('../drawing_shapes' ))
print(os.listdir(os.curdir))
print(os.curdir)
print('\n')

print(os.chdir('../drawing_shapes'))
print(os.getcwd())
writeFile = open('test.txt', 'w')