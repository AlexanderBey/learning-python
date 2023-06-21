# Tuples
# you can do everything with tuples that you can 
# do with lists except modify them

x = ('a', 'b', 'c')

print(x[2])
print(x[1:])
print(len(x))
print(max(x))
print(min(x))
print(5 in x)
print(5 not in x)

print(x + x)

print(x * 3)

# Packing and unpacking tuples

one, two, three, four = 1, 2, 3, 4

# This technique is a convient way to swap variables

var1, var2 = 1, 2
print(var1, var2)

var1, var2 = var2, var1
print(var1, var2)

# using * to grab excess items

x = (1, 2, 3, 4)

a, b, *c = x
print(a, b, c)

a, *b, c = x
print(a, b, c)

# converting between lists and tuples
converted_list = list((1, 2, 3))
print(converted_list)

converted_tuple = tuple([1, 2, 3])
print(converted_tuple)

#Quick check: Tuples

x = (3,1,4,2)

# Convert the tuple to a list, sort the list, 
# and convert it back to a tuple

sorted_x = tuple(sorted(list(x)))
