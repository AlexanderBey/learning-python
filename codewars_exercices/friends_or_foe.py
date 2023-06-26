def friend(friends_list):

    true_friends = []
    for friend in friends_list:
        if len(friend) == 4:
            true_friends.append(friend)

    return true_friends

print(friend(["Ryan", "Kieran", "Mark",]))