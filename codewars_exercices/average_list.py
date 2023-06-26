def find_average(numbers):
    sum = 0
    if len(numbers) == 0:
        return 0
    
    for number in numbers:
        sum += number
    return sum / len(numbers)

print(find_average([1,2,3,4,5]))

# More concise solution:

#def find_average(array):
#    return sum(array) / len(array) if array else 0
# print(find_average([1,2,3,4,5]))
