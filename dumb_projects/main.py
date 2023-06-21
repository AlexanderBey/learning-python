
import random


# structure:

# 1. Initiate and shuffle deck
# 2. pop 2 cards from deck
# 3. river time 3 cards
# 4. turn time 1 card
# 5. river time 1 card
# 6. find pairs in player hand
# 7. find pairs in community cards
# 8. find pairs in player hand and community cards


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank 

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8' ,'9' ,'10', 'jack','Queen','King']
        self.deck = [(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self, cards):
        self.cards = cards

    def find_pairs(self):
        pass
    

class Game: 
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.community_cards = []
    def play(self):
        # Game logic goes here
        pass


if __name__ == '__main__':
    game = Game()
    game.play()
