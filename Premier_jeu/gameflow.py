#code pour le poker

#importation de module
import random as rd

#fonction pour creer le deck
def deck_generator():
    deck = {}
    colors = ['spades', 'hearts', 'diamonds', 'clubs']
    values = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    j = 0
    for i, val in enumerate(colors):
        for k, valeur in enumerate(values):
            deck[str(j)] = [val, valeur]
            j+= 1
    return deck
deck = deck_generator()
print(deck)

#fonction pour melanfer le deck
def shuffle_deck():
    return rd.sample(range(52), 51)


a = shuffle_deck()
print(deck[str(a[0])])
print(deck[str(a[1])])
print(deck[str(a[2])])