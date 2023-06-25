def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False
    

print(check([1,2,3], 3))
print(check([1,2,3], 4))


# Better way 
# def check(seq, elem):
#     return elem in seq
# 
# print(check([1,2,3], 3))
# print(check([1,2,3], 4))
