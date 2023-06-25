def minimum(arr):
    minimum = arr[0]
    for number in arr:
        if number < minimum:
            minimum = number

    return minimum

def maximum(arr):
    maximum = arr[0]
    for number in arr:
        if number > maximum:
            maximum = number

    return maximum


print(minimum([1,2,3,4,5]))
print(maximum([1,2,3,4,5]))

# better solution
# def minimum(arr):
#     return min(arr)

# def maximum(arr):
#     return max(arr)