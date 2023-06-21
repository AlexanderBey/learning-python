'''
----------------------------------
print("having fun with dictionaries")
----------------------------------

y = {}

y[0] = "Hello"
y[1] = "Goodbye"

print(y)


print(y[0])

print(y[1] + "friend")

y["two"] = 2
y['pi'] = 3.14
y["two"] * y["pi"]

english_to_french = {}
english_to_french["red"] = "rouge"
english_to_french["blue"] = "bleu"
english_to_french["green"] = "vert"
print("red is", english_to_french["red"])
'''

'''
# Exercice 1
print("Welcome to the programme")
print('\n')

dictionary = {}
for i in range(3):
    user_name = input("Please enter a name: ")
    user_age = input("Please enter an age: ")
    dictionary[user_name] = user_age
    print('\n')

print("What name would you like to look up?")

user_name = input("Enter a name to check the age: ")
while user_name not in dictionary:
    print('\n')
    print(f"{user_name} is not in the dictionary.")
    user_name = input("Please enter a valide name : ")
   
print('\n')
print(f"The age of {user_name} is {dictionary[user_name]}")

'''

'''
car_colors = {'toyota': "red", 'ford': "blue", 'bmw': "green"}
print(car_colors)
# print(len(car_colors))

keys_in_a_dictionary = list(car_colors.keys())
print('The keys of the dictionary are:', keys_in_a_dictionary)

values_in_a_dictionary = list(car_colors.values())
print('The values of the dictionary are:', values_in_a_dictionary)

print('\n')

# return a list of tuples
# It return the key value pair of the dictionary

items = list(car_colors.items())
print(items)

# Let's try to delete an element from the dictionary using the key
del car_colors['toyota']
print(car_colors)


# Now time for error handling
# You check the key to see if it exists in the dictionary
print('ford' in car_colors)
print('lost_car' in car_colors)

# You can also use the get method to check if a key exists in a dictionary
# it return the value stored in the key if it exists
# if it doesn't exist, it return the default value
# Otherwise, it returns None
print(car_colors.get('ford', 'no car found'))
print(car_colors.get('lost_car', 'no car found'))
print(car_colors.get('lost_car'))


# Trying out the update method
z = {1: "one", 2: "two"}
x = {0: "zero", 1: "un"}

x.update(z)
print(x)

# Exercice 2
x = {'a':1, 'b':2, 'c':3, 'd':4}
y = {'a':6, 'e':5, 'f':6}



del x['d']
z = x.setdefault('g', 7)

# Faire attention 
# c'est x qui est modifié par y et non l'inverse
x.update(y)
print(x)

'''

print('-'*15)
print("Word counting")
print('-'*15)

sample_string = "To  to to to to be or not to be"
occurence = {}

for word in sample_string.split():
    occurence[word] = occurence.get(word, 0) + 1

for word in occurence:
    print("The word", '"', word, '"', "occurs", occurence[word], \
          "times in the string")


"""
The matrix thing doesn't work

print('-'*15)
print("Sparse matrices")
print('-'*15)
   #0 #1 #2 #3
#0 [3 0 -2 11] 
#1 [0 9  0 0 ] 
#2 [0 7  0 0 ] 
#3 [0 0  0 -5] 
# (y,x) = (0,0)

matrix = {(0,0): 3, (0,2): -2, (0,3): 11, 
          (1,1): 9, (2,1): 7, (3,3): -5}

# Now you can access an individual matrix element 
# at a given row and column number by this bit of code

if (rownum, colnum) in matrix: 
    element = matrix[(rownum, colnum)]
else:
    element = 0
"""

'''
didn't understand this shitty concept

print('-'*15)
print("Using dictionaries as caches")
print('-'*15)

def sol(m, n, t):
    
    for i in range(1000):
        result = m + n + t
        print('sol i=', i, result)
    print('finished')
    


sole_cache = {}
def sole(m, n, t):
    for i in range(1000):
        if (m, n, t) in sole_cache:
            return sole_cache[(m, n, t)]
        else:
            result = m + n + t
            sole_cache[(m, n, t)] =  result   
            print('sole i=', i, result)
    print('finished')

# This is stuck in an infinite loop
# sol(1, 2, 3)

#how can we fix this?
sole(1, 2, 3)
'''

print('-'*15)
print("Efficiency of dictionaries")
print('-'*15)