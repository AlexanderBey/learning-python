def are_you_playing_banjo(name):

    if (name.startswith('R')) or (name.startswith('r')):
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'

print(are_you_playing_banjo('Amy')) # NO
print(are_you_playing_banjo('Ringo'))# YES
print(are_you_playing_banjo('roger'))# YES

