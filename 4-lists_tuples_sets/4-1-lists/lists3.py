inv = [
    'Sword',
    'Shield',
    'Potion of Invisibility',
    'Map'
]

# enumerate returns a tuple with the index and the item
'''
inv = [
    (0, 'Sword'),
    (1, 'Shield'),
    (2, 'Potion of Invisibility'),
    (3, 'Map')
]
'''

for index, item in enumerate(inv):
    print(item)