from locness import locness
import string

"""
x = "hello"

# just slicing the hello sting
print("----------------")
print("TESTING SLICES")
print("----------------")
print("\n")
print("[Original slice] ->", x)
print("[Output of the splice] ->", x[:])
print("\n")
# Slice the \n from the text


print("----------------")
print("SOMETHING ELSE")
print("----------------")

y = "Goodbye\n"
print(y[:-1])



print("\n")
print("----------------")
print("FUN WITH LEN FUNCTION")
print("----------------")


def length(word):
    word_length = len(word)
    print(f"The word is {word}")
    print(f"It's {word_length} character long")
    return word_length

length('bob')

print("\n")

print("----------------")
print("ADDING STRINGS")
print("----------------")

adding_string = "Coffe" + " " + "Machine"
print(adding_string)

print(8 * 'c')


locness()

string = "bob"
function = string.encode()
print(function)


print("--------------------")
print("SPLIT AND JOIN")
print("--------------------")

# Splitting a string

string = "hello,this,is,my,string"
print("This is the string ->", string)
result = string.split(',')
print("This is the string now ->", result)

print("\n")
# Joining a string
print("Time to join them back together!")
separator = ' '
joined_string = separator.join(result)
print("Joined back together again -> ", joined_string)


# Challenge completed
string3 = "this is a test"
string3 = string3.replace(" ", "-")
print(string3)
print("Challenge finished Congrats \N{winking face}")

print("\n")
print("-------------------------------")
print("Converting strings to numbers")
print("-------------------------------")

"""

""" You need to check that later what are base in math and learn why this doesn't work"""

""""
# result_2 = int('a1')
# result_3 = int('12G', 16)
# result_4 = float("12345678901234567890")
# result_5 = int("12*2")

# print(result_4)

print("\n")
print("-------------------------------")
print("Getting rid of extra whitespace")
print("-------------------------------")

url = "www.python.org"
url2 = url.strip("w")
print(url2)

url3 = url.strip(".gorw")
print(url3)

print("\n")
print("-------------------------------")
print("String searching")
print("-------------------------------")

string_8 = "Mississippi"

find = string_8.find("ss")
print("This is find ->", find)
find2 = string_8.find("ss", 0, 6)
print("This is find with a start and end argument ->", find2)
find3 = string_8.rfind("ss")
print("This is rfind ->", find3)

print('\n')

print("Does mississippi start with Miss? ", string_8.startswith("Miss"))
print("Does mississippi start with Mist? ", string_8.startswith("Mist"))

print("Does mississippi ends with pi? ", string_8.endswith("pi"))
print("Does mississippi ends with p? ", string_8.endswith("p"))


# Exercise 

dumb_string = "i don't like being rejected"
print("Does dumb_string ends with rejected? ", dumb_string.endswith("rejected"))
"""
"""
x = "Mississippi"
x_replace = x.replace("ss", "++")
print(x_replace) 
"""

"""
print("\n")
print("-------------------------------")
print("maketrans function")
print("-------------------------------")

x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")

translated_table = x.translate(table)
print(x)
print(translated_table)

print("time to reverse it my friend")

string_10 = "hello THIS is The test Of your LIFE"
string_10 = string_10.swapcase()
print(string_10)
"""

'''
print("\n")
print("-------------------------------")
print("List manipulation")
print("-------------------------------")

text = "Hello, World"
numbers = len(text)
index = []

for i in range(numbers):
    string_number = str(i)
    index.append(string_number)

wordList = list(text)
print(text)
print(wordList)
print(index)

print("\n")

wordList[5:] = []
print(wordList)
print(index)

wordList.reverse()
# Convert the list back into a string
text = "".join(wordList)
print(text)

string_11 = "Remove!this!punctuation!please!"
print(string_11)
string_11 = string_11.replace("!", " ")
print(string_11)


x = "123"
x_digit = x.isdigit()
x_alpha = x.isalpha()

print(x_digit)
print(x_alpha)


x = 'M'
x_lower = x.islower()
x_upper = x.isupper()

print(x_lower)
print(x_upper)

'''

'''
locness()
# Exercise 1
x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
print(x)

for i in range(len(x)):
    print(x[i])
    x[i] = x[i].strip('"')

print(x)

# Exercise 2
word = "Mississippi"
print(word)
find_r = word.rfind("p")
word = word[:find_r] + word[find_r + 1:]

print(find_r)
print(word)
'''

'''
locness()

print("\n")
print("-------------------------------")
print("Converting from objects to strings")
print("-------------------------------")



conversion = repr([1, 2, 3])
print(type(conversion))
print(conversion)

list = [1, 2, 3]
print(type(list))
print(list)

x = 27
y = 'bob'
z = 1.2
vev = True

repr(x)
repr(y)
repr(z)
repr(vev)
'''

'''

locness()
print("\n")
print("-------------------------------")
print("format method and positional parameters")
print("-------------------------------")


string_13 = "{0} is the {1} of {2}".format("Ambrosia", "food", "the gods")
print(string_13)

string_13 = "{{Ambrosia}} is the {0} of the {1}".format("food", "gods")
print(string_13)

string_14 = "{say}, it's {name} !".format(say = 'Say my name', name = 'Walter White')
print(string_14)


# Exercise 1
x_1 = "{1:{0}}".format(10, 4)
x_2 = "{0:$>5}".format(3)
x_3 = "{a:{b}}".format(a=1, b=5)
x_4 = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)

print(x_1)
print(x_2)
print(x_3)
print(x_4)

'''

'''
locness()
print("\n")
print("-------------------------------")
print("Learn how to print")
print("-------------------------------")

print(('a','b','c'), sep= '|', end=' ')
print("This is the story of bob \n bob made a new friend. \n Now it's time for bob to let go", file=open('testfile.txt', 'w'))
'''

print("-------------------------------")
print("String interpolation")
print("-------------------------------")
locness()


value = 42
message = f"The answer of life is {value}"
print(message)

pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
message = f"The value of pi is {pi:.3f}"
print(message)