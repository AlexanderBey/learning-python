import copy

# Original list
original_list = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow_copy = copy.copy(original_list)

# Deep copy
deep_copy = copy.deepcopy(original_list)

# print("Original list before modification:", original_list)

# Modify the first element in the original list 
original_list[0][0] = 99

# Print the original list
# print("Original list after modification:", original_list)
# print("shallow copy:", shallow_copy)
# print("deep copy:", deep_copy)


new_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
deep_copy_new_list = copy.deepcopy(new_list)
print(new_list)
print(deep_copy_new_list)

print('\n')
deep_copy_new_list[0][0] = 99
print(new_list)
print(deep_copy_new_list)