class TCard():
  def __init__(self,Suit,Rank):
    self.Suit = Suit
    self.Rank = Rank

def CreateDeck(Deck):
    for suit in range(1,5):
        for rank in range(1,14):
            Deck.append(TCard(suit,rank))
    return Deck

def OutputCard(Card):
    if Card.Suit == 1:
        suit = "♣"
    elif Card.Suit == 2:
        suit = "♦"
    elif Card.Suit == 3:
        suit = "♥"
    elif Card.Suit == 4:
        suit = "♠"

    if Card.Rank == 1:
        rank = "A"
    elif Card.Rank == 11:
        rank = "J"
    elif Card.Rank == 12:
        rank = "Q"
    elif Card.Rank == 13:
        rank = "K"
    else:
        rank = Card.Rank
    return f'{rank} {suit}'

Deck = []
Deck = CreateDeck(Deck)
import random
r = random.randint(0, 51)
print(OutputCard(Deck[r]))
