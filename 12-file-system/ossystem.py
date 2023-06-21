import os
import sys

if os.name == 'posix':
    root_dir = '/'
elif os.name == 'nt':
    root_dir = 'C:\\'
else:
    print('Unknown OS')
    root_dir = None

print(root_dir)
print(sys.platform)

