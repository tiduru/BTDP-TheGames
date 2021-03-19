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


#création de la liste avec toutes les carte
nb_joueurs = 2 #nombre de joueur provenant du serveur de Tim
mains = [[str(shuffle[2 * nb_joueurs]), str(shuffle[2 * nb_joueurs + 1]), str(shuffle[2 * nb_joueurs + 2]), str(shuffle[2 * nb_joueurs + 4]), str(shuffle[2 * nb_joueurs + 6])]]

#Gestion des mises
#banques     List avec les montant de tous les joueurs
#mises       List avec le total des mises de la main et de chaque joueur
#b_blind     Montant de la Big blind
#s_blind     Montant de la Small blind

banque = 1000  #montant fixer dans les parametres du jeu
b_blind = 250  #montant fixer dans les parametre du jeu
s_blind = 100  #montant fixer dans les parametre du jeu



#initialisation des mise
joueurs = []
mise = 0
for i in range(nb_joueurs):
    main_joueur = [str(shuffle[i]), str(shuffle[i+nb_joueurs])]
    joueurs.append([main_joueur, banque, mise, True])
    mains.append(main_joueur)

#fonction qui fait la gestion des tour de mise
def tour_de_mise():
    for i in range(nb_joueurs):
        if joueurs[i][3]:
            # pop le menu d'action au joueur
            if mise <= joueurs[i][1]:
                joueurs[i][2] = joueurs[1][2] + mise # valeur de la mise entrer par le joueur
                joueurs[i][1] = joueurs[i][1] - mise # actualisation de la banque du joueur
            else:
                #afficher un message d'erreur montant trop eleve
                #le joueur doit entrer un nouveau montant
            joueurs[i][3] = True_or_False #True si le joueur entre un mise ou check, False si le joueur fold
    return joueurs

#game_on valeur qui dit qu'on joue un main de poker
while game_on:
    #montrer les cartes aux joueurs
    #debut premier tout de mise
    tour_de_mise()
    #fin premier tour de mise
    #montrer les 3 premiere carte du paquet commun
    #debut 2e tour de mise
    #fin 2e tour de mise
    #montrer la 4e carte
    #debut 3e tour de mise
    #fin 3e tour de mise
    #montrer la 5e carte
    #debut 4e tour de mise
    #fin 4e tour de mise
    #calcul de la main gagnante
    #Distribution du cash






#Pour inedxer dans deck et afficher les cartes
'''for i in range(5):
    print(deck[mains[0][i]])
for i in range(2):
    print(deck[mains[1][i]])'''

