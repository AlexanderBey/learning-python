from functools import lru_cache

@lru_cache #lru ="least recently used"
def increment(num):
    print('Running 1000 lines of code')
    return num + 1

print(increment(1))
print(increment(2))
print(increment(3))
print(increment(1))


# lru cache runs the code and ignore the 1000 lines of code and return the value from the cache