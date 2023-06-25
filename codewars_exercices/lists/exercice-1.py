'''
Complete the square su m function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9
'''

def square_sum(numbers):
    sum = 0
    for number in numbers:    
        number = number ** 2
        sum += number
    return sum

square_test = square_sum([1,2,2])

print(square_test)