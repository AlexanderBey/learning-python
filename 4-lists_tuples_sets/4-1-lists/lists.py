def remove(item):
    if item in list:
        list.remove(item)
        print(list)
    else:
        print("Item not found")

def removeDuplicates(item):
    if item in list:
        count_occurence = list.count(item)
        print(count_occurence)
        if count_occurence == 1:
            print("No duplicates found")
            return
        if count_occurence > 1:
            print("Duplicates found")
            print("Removing duplicates")
            for _ in range(count_occurence - 1):
                list.remove(item)
        print(list)
    else:
        print("Item not found")

# 5 is here 4 times, should return 4 
# Cool it works

list = [1, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5]

# remove(4)
removeDuplicates(5)
removeDuplicates(2)