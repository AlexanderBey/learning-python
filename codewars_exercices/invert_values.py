def invert(list_of_numbers):
    inverted_list_of_numbers = []
    for number in list_of_numbers:
        number = -number
        inverted_list_of_numbers.append(number)

    return inverted_list_of_numbers

print(invert([1,-2, 3]))
print(invert([-1, 2, -3]))


# Better way:
#  
# def invert(lst):
#     return [-x for x in lst]
