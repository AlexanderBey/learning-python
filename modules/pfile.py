import mymath, importlib
from new_math import *
importlib.reload(mymath)

print(mymath.pi)
print(mymath.area(2))
print(mymath.__doc__)

import sys
sys.path

new_divide()

print(locals())



