
import collections

Card = collections.namedtuple('Card', ['rank', 'suits'])

class CardGame:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
        
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]

Enock = Card('8', 'hearts')

Card('7', 'diamonds')
Card('6', 'clubs')
Card('4', 'spades')

deck = CardGame()

print(len(deck))

print(deck[1])