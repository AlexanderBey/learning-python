def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    else: 
        return "Player 2 won!"

# Player 1 win conditions    
print('-' * 50)
print('Player 1 win conditions')
print('-' * 50)
print(rps('rock', 'scissors'))
print(rps('scissors', 'paper'))
print(rps('paper', 'rock'))

print('\n')

# Draws
print('-' * 50)
print('Draws condtition')
print('-' * 50)
print(rps('rock', 'rock'))

print('\n')


# Player 2 wins
print('-' * 50)
print('Player 2 win conditions')
print('-' * 50)

print(rps('rock', 'paper'))
print(rps('scissors', 'rock'))
print(rps('paper', 'scissors'))


# better solution
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

