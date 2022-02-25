from flask import Flask
app = Flask(__name__)

import deck     # from deck.py

Deck = []
index = -1
Deck = deck.CreateDeck(Deck)
Deck = deck.ShuffleDeck(Deck)

@app.route('/')
def home():
    global index
    index = index + 1
    return str(index) + " : " + str(deck.GetCard(Deck, index))
