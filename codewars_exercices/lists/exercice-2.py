'''Remove First and Last Character'''

def remove_char(s):
    list_of_characters = list(s)
    print(list_of_characters)
    list_of_characters.pop(0)
    list_of_characters.pop(-1)

    return ''.join(list_of_characters)
    
print(remove_char('bob'))


# better solution
# def remove_char(s):
#     return s[1:-1]
#
