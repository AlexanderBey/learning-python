def get_sum(a, b):
    if a == b:
        return a 
    else:
        if a < b:
            return sum(range(a, b + 1))
        else:
            return sum(range(b, a + 1))
        
print(get_sum(0, 3))
print(get_sum(5, -1))


