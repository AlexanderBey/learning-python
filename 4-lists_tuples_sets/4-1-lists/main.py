strings = []
numbers = []

list = ['e', 'x', 'H', 9, 'A', 'Y', 'u', 2, 'N', 'w', 42 , 78 , 't']

for item in list:
    print("current item", item) 
    if isinstance(item, str):
        strings.append(item)
        print(item , " has been added to the string list")

    if isinstance(item, int):
        numbers.append(item)
        print(item , " has been added to the numbers list")
    print("\n")

    

print("the strings list contains:",strings)
print("the numbers list contains:",numbers)


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2 =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']


for item in alphabet:
    print('\n')
    print('---------')
    print("current item", item)
    print('---------')
    
    if item in list2:
        print(item , " is in the list")
    if item not in list2:
        print(item , " is not in the list")


def funct1(x, y, z):
    value = x + 2*y + z**2

    if value > 0:
        return x + 2*y + z**2
    else: 
        return 0
    

u,v = 3, 4
"""
calling = funct1(u, v, 2)
print(calling)

calling2 = funct1(u, z=v, y=2)
print(calling2)



def funct2(x, y=1, z=1):
    print('x:', x)
    print('y:', y)
    print('z:', z)
    return x + 2*y + z**2
calling3 = funct2(3)
calling4 = funct2(3, z=4)

print(calling3)
print(calling4)

"""

def funct3(x, y=1, z=1, *tup):
    print((x,y,z) + tup)
    print("This is the tuple that collect the garbage : ", tup)
    print('\n')
print('----------------')
print("this is func 3")
funct3(2)
funct3(1,2,3,4,5,6,7,8,9)



def funct4(x,y=1,z=1, **kwargs):
    print(x, y, z, kwargs)
    print("This is the dictionnary that collect the garbage : ", kwargs)

funct4(1,2,m=5,n=9,z=3)






