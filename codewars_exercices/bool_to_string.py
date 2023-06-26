def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    else:
        return "No"
    

print(bool_to_word(True))
print(bool_to_word(False))


# Better way:

#def bool_to_word(bool):
#    return "Yes" if bool else "No"


#print(bool_to_word(True))
#print(bool_to_word(False))