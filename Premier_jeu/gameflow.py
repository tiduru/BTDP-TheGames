#code pour le poker

#importation de module
import random as rd

#fonction pour creer le deck
#deck       Librairy avec toutes les cartes
def deck_generator():
    deck = {}
    colors = ['spades', 'hearts', 'diamonds', 'clubs']
    values = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    j = 0
    for i, val in enumerate(colors):
        for k, valeur in enumerate(values):
            deck[str(j)] = [valeur, val]
            j+= 1
    return deck
deck = deck_generator()


#fonction pour melanger le deck
def deck_shuffler():
    return rd.sample(range(52), 51)

shuffle = deck_shuffler()


#création de la matrice avec toutes les carte
nb_joueurs = 2 #nombre de joueur provenant du serveur de Tim
mains = [[str(shuffle[2 * n]), str(shuffle[2 * n + 1]), str(shuffle[2 * n + 2]), str(shuffle[2 * n + 4]), str(shuffle[2 * n + 6])]]

for i in range(n):
    main_joueur = [str(shuffle[i]), str(shuffle[i+n])]
    mains.append(main_joueur)

#Gestion des mises
#banques     List avec les montant de tous les joueurs
#mises       List avec le total des mises de la main et de chaque joueur
#b_blind     Montant de la Big blind
#s_blind     Montant de la Small blind




#Pour inedxer dans deck et afficher les cartes
'''for i in range(5):
    print(deck[mains[0][i]])
for i in range(2):
    print(deck[mains[1][i]])'''

