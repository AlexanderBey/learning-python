
"""
print('-' * 50)
print("Basinc syntax for a python function")
print('-' * 50)

person_dictionary = {}
def person(name, age):
    print("My name is", name, "and my age is", age)
    person_dictionary[name] = age

person("Bob", 35)
person("Alice", 27)
print(person_dictionary)


'''passing a list as an argument to a function '''
'''Those changes are directly assigned to the original list'''


def modify_list(lst):
    lst.append(100)

def modify_dict(dct):
    dct['new_key'] = 'new_value'

a = [1, 2, 3]
b = {'key': 'value1'}

modify_list(a)
modify_dict(b)

print(a)
print(b)


'''This one will not assign to the original list '''

def not_modify_list(lst):
    lst = [100, 200, 300] # This is a new list
    print("new list: ", lst)

def not_modify_dict(dct):
    dct = {'new_key': 'new_value'} # This is a new dictionary
    print("new dict: ", dct)

a = [1, 2, 3]
b = {'key': 'value1'}

not_modify_list(a)
not_modify_dict(b)

print('old : ', a)
print('old : ', b)


''' global and non local variables'''






print('\n')

print('-' * 50)
print("Without nonlocal statement")
print('-' * 50)


x = 0 # this is a global variable

def outer():
    x = 10 # This is a local variable, local to 'outer'
    print("outer:", x)
    def inner():
        #nonlocal x
        x = 20 # This is still local to 'outer', 
        # but can be changed inside 'inner'
        print("inner:", x)

    inner()
    print("outer-2:", x) # x is now 20


outer()
print("global:", x) # x is still 0

print('\n')

print('-' * 50)
print("With nonlocal statement")
print('-' * 50)

def outer2():
    x = 10 # This is a local variable, local to 'outer'
    print("outer:", x)
    def inner():
        nonlocal x
        x = 20 # This is still local to 'outer', 
        # but can be changed inside 'inner'
        print("inner:", x)

    inner()
    print("outer-2:", x) # x is now 20


outer2()
print("global:", x) # x is still 0


print('\n')
print('-' * 50)
print("Test")
print('-' * 50)




def multiply(a):
    
    def add(a):
        result = a + 2
        print('result in the add function: ', result)
        return result

    added = add(a)

    result = a * added
    print('result in the multiply function: ', result)
    return result


print(multiply(5))



def simple_generator():
    i = 0
    while True:        
        yield i
        i += 1

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))


# check out decorators later, didn't understand that concept yet

print('\n')
print('-' * 50)
print("Decorators")
print('-' * 50)

def bob():
    return "bob is ordinary"


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        pif = func()
        print(pif)
        print("Something is happening after the function is called.")
    return wrapper


bob = my_decorator(bob)
bob()

"""
