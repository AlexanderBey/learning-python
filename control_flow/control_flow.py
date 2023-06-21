someList = [(1, 2), (3, 7), (9, 5)]
result = 0
for t in someList:
    result = result + (t[0] * t[1])


# cleaner way to do it
result = sum([t[0] * t[1] for t in someList])

# enumerate function

x = [1, 3, -7, 4, 9, -5, 4]
for i, n in enumerate(x):
    if n < 0:
        print("Found a negative number at index ", i)


# keep reading chapter 8 of the book, 
# Because i got so fucking bored from reading the rest