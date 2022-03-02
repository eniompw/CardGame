from flask import Flask, render_template
app = Flask(__name__)

import deck     # from deck.py

Deck = []
index = 0
Deck = deck.CreateDeck(Deck)
Deck = deck.ShuffleDeck(Deck)

@app.route('/')
def home():
    global index
    player = []
    for i in range(5):
        player.append(deck.GetCard(Deck, index))
        index = index + 1
    return render_template('cards.html', player=player)
