'''swap the item in the list into the first position'''

hotbar = [
    'Torch',
    'Rock',
    'Potion',
    'Sword',
    'Shield',
]

# Step 1: Get the index of sword
index = hotbar.index('Sword')
print(index)

# Step 2: pop the item from the hotbar list 
# and save it into item
item = hotbar.pop(index)
print(item)
print(hotbar)

# Step 3: Put the item back at index 0
# insert takes an index and the thing you want to insert
hotbar.insert(0, item)
print(hotbar)