
x = set([1, 2, 3, 1, 3, 5])
print(x)

x.add(6)
print(x)

print(1 in x)
print(4 in x)

y = set([1, 7, 8, 9])

print(x | y)
print(x & y)
print(x ^ y)


# Frozen sets
x = set([1, 2, 3, 4])
y = frozenset(x)

print(y)

x.add(y)
print(x)


new_set = set([1,2,5,1,0,2,3,1,1,(1,2,3)])
print(new_set)

print(len(new_set))
