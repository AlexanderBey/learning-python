'''import random
import time
import matplotlib.pyplot as plt

rainbow_colors = [
    "\033[31m",  # Red
    "\033[91m",  # Light Red
    "\033[33m",  # Yellow
    "\033[32m",  # Green
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[95m"   # Light Magenta
]




list_of_numbers = []

def randomSelection():

    i = 0
    z = 0
    while i < 1000000:

        if z == 50000:
            print("One mile stone reached")
            time.sleep(3)
            z = 0
        number = random.randint(0, 50)
        random_color = random.choice(rainbow_colors)
        print(random_color + "-" * 50 + "\033[0m")
        print('*' * number)
        print(random_color + "-" * 50 + "\033[0m")
        print('\n')

        list_of_numbers.append(number)
        i += 1
        z += 1
        print("i == " + str(i))

randomSelection()

print(list_of_numbers)
list_of_numbers.sort()
print('sorted')
print(list_of_numbers)


dictionary_of_occurences = {}
for number in list_of_numbers:
    count = list_of_numbers.count(number)
    dictionary_of_occurences[number] = count

del list_of_numbers

print('\n')
print("-" * 50)
print("Welcome to random number generator")
print("-" * 50)

print(dictionary_of_occurences)

# Get the keys (numbers) and values (occurences) from the dictionary
sorted_occurences = sorted(dictionary_of_occurences.items(), key=lambda x: x[1])
sorted_dictionary = dict(sorted_occurences)

# Get the keys (numbers) and values (occurrences) from the sorted dictionary
numbers = list(sorted_dictionary.keys())
occurrences = list(sorted_dictionary.values())

# Plot the bar chart
plt.bar(numbers, occurrences)
plt.xlabel('Numbers')
plt.ylabel('Occurrences')
plt.title('Occurrences of Numbers')
plt.show()
'''

import random
import time
import matplotlib.pyplot as plt

rainbow_colors = [
    "\033[31m",  # Red
    "\033[91m",  # Light Red
    "\033[33m",  # Yellow
    "\033[32m",  # Green
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[95m"   # Light Magenta
]

sole_cache = {}

def sole(m, n, t):
    if (m, n, t) in sole_cache:
        cached_result, cached_color = sole_cache[(m, n, t)]
        return cached_result, cached_color
    else:
        random_color = random.choice(rainbow_colors)
        result = m + n + t
        sole_cache[(m, n, t)] = (result, random_color)
        return result, random_color

def randomSelection():
    start_time = time.time()  # Record start time
    i = 0
    z = 0
    time_list = []
    while i < 100000:
        if z == 1000:
            print("One milestone reached")
            elapsed_time = time.time() - start_time  # Calculate elapsed time
            print(f"Time elapsed: {elapsed_time:.2f} seconds")
            time_list.append(elapsed_time)
            #Reset 
            z = 0
            start_time = time.time()  # Reset start time

        m = random.randint(0, 10)
        n = random.randint(0, 10)
        t = random.randint(0, 10)
        result, random_color = sole(m, n, t)  # Use cached values
        print(random_color + "-" * 50 + "\033[0m")
        print('*' * result)
        print(random_color + "-" * 50 + "\033[0m")
        print('\n')

        i += 1
        z += 1
        print("i == " + str(i))
    for item in time_list:
        print(item)
randomSelection()


# Rest of the code...
'''
list_of_numbers = []
for _ in range(1000000):
    number = random.randint(0, 50)
    list_of_numbers.append(number)

dictionary_of_occurrences = {}
for number in list_of_numbers:
    count = list_of_numbers.count(number)
    dictionary_of_occurrences[number] = count

del list_of_numbers

print('\n')
print("-" * 50)
print("Welcome to random number generator")
print("-" * 50)

print(dictionary_of_occurrences)

# Get the keys (numbers) and values (occurrences) from the dictionary
sorted_occurrences = sorted(dictionary_of_occurrences.items(), key=lambda x: x[1])
sorted_dictionary = dict(sorted_occurrences)

# Get the keys (numbers) and values (occurrences) from the sorted dictionary
numbers = list(sorted_dictionary.keys())
occurrences = list(sorted_dictionary.values())

# Plot the bar chart
plt.bar(numbers, occurrences)
plt.xlabel('Numbers')
plt.ylabel('Occurrences')
plt.title('Occurrences of Numbers')
plt.show()
'''