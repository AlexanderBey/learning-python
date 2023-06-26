def is_square(n):
    if n < 0:
        return False
    else:
        print(n ** 0.5)
        print(int(n ** 0.5))
        return n ** 0.5 == int(n ** 0.5)
    
print()
print(is_square(4))
print(is_square(25))
print(is_square(5))
