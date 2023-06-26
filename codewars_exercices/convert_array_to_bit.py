'''
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [0, 0, 1, 0] ==> 2
Testing: [1, 0, 0, 1] ==> 9
Testing: [1, 0, 1, 1] ==> 11
Testing: [1, 1, 1, 1] ==> 15

'''

def binary_array_to_number(arr):

    print(len(arr))

binary_array_to_number([0,0,0,0])



'''
[0,0,0,0] = 0

[0,0,0,1] = 1² = 1

[0,1,0,0] = 2² = 4
[1,0,0,1] = 3² = 9
'''

# def binary_array_to_number(arr):
#     # your code
#     # return int("".join(map(str, arr)), 2)
#     return int("".join(str(i) for i in arr), 2)
