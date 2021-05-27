#code pour le poker

#importation de module
import random as rd
import collections

#fonction pour creer le deck
#deck       Librairy avec toutes les cartes
def deck_generator():
    deck = {}
    colors = ['spades', 'hearts', 'diamonds', 'clubs']
    symbol = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    valeur = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    j = 0
    for i, couleur in enumerate(colors):
        for k, symbole in enumerate(symbol):
            deck[str(j)] = [symbole, couleur, valeur[k]]
            j += 1
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
    #format joueurs : main_joueur = ses cartes; banque=montant d'argent restant;
    #                 mise = montant misé; 0 = valeur de la main initialement 0;
    #                 True = si le joueur a peut encore miser ou non
    joueurs.append([main_joueur, banque, mise, 0, True])
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
                pass
            #joueurs[i][3] = True_or_False    #True si le joueur entre un mise ou check, False si le joueur fold

    return joueurs

#vérification des mains
def check_straight_flush(hand):
    suite = check_suite(hand)
    if suite[0]:
        if check_flush(suite[1]):
            return True
    return False

def check_carre(hand):
    val = []
    for i in range(len(hand)):
        val.append(deck[hand[i]][0])
    for i, carte in enumerate(val):
        occurence = val.count(carte)
        if occurence == 4:
            return True
    return False

def check_full_house(hand):
    if check_pair(hand) and check_triple(hand):
        return True
    return False

def check_flush(hand):
    val = []
    for i in range(len(hand)):
        val.append(deck[hand[i]][1])
    for i, carte in enumerate(val):
        occurence = val.count(carte)
        if occurence >= 5:
            return True
    return False

def check_suite(hand):
    val = []
    for i in range(len(hand)):
        val.append(deck[hand[i]][2])

    count = 0
    suite = []
    val = sorted(val)
    for i in range(len(val)-1):
        if (val[i+1] == val[i] + 1) and i == len(val) - 2:
            count += 2
            for j in range(len(hand)):
                if deck[hand[j]][2] == val[i]:
                    suite.append(hand[j])
            for j in range(len(hand)):
                if deck[hand[j]][2] == val[i+1]:
                    suite.append(hand[j])

        elif val[i+1] == val[i] + 1:
            count += 1
            for j in range(len(hand)):
                if deck[hand[j]][2] == val[i]:
                    suite.append(hand[j])

        elif (val[i+1] != val[i] + 1) and count < 5:
            count = 0
            suite = []
    if count >= 5:
        return True, suite
    return False, suite

def check_triple(hand):
    val = []
    for i in range(len(hand)):
        val.append(deck[hand[i]][0])
    for i, carte in enumerate(val):
        occurence = val.count(carte)
        if occurence == 3:
            return True
    return False

def check_double_pair(hand):
    val = []
    count = 0
    for i in range(len(hand)):
        val.append(deck[hand[i]][0])
    for i, carte in enumerate(val):
        occurence = val.count(carte)
        if occurence == 2:
            count += 1
        if occurence == 2 and count == 4:
            return True
    return False

def check_pair(hand):
    val = []
    for i in range(len(hand)):
        val.append(deck[hand[i]][0])
    for i, carte in enumerate(hand):
        occurence = hand.count(carte)
        if occurence == 2:
            return True
    return False



#fonction qui attribue une valeur aux mains des joueurs
def check_hand(hand):
    if check_straight_flush(hand):
        return 9
    if check_carre(hand):
        return 8
    if check_full_house(hand):
        return 7
    if check_flush(hand):
        return 6
    if check_suite(hand)[0]:
        return 5
    if check_triple(hand):
        return 4
    if check_double_pair(hand):
        return 3
    if check_pair(hand):
        return 2
    return 1

#fonction qui indique quel joueur gagne la main
def winning_hand(hand):
    val = []
    main_joueur = []
    center = []
    joueur = []
    for i in range(nb_joueurs+1):
        if i == 0:
            for j in range(5):
                center.append(hand[i][j])
        elif i != 0:
            for j in range(5):
                main_joueur.append(center[j])
            for j in range(2):
                main_joueur.append(hand[i][j])

            val.append(check_hand(main_joueur))
            joueur.append([i, hand[i], val[i-1]])
            main_joueur = []


    val = sorted(val)
    winner = val[-1]
    for i in range(nb_joueurs):
        if winner == joueur[i][2]:
            return joueur[i]





#hand = ['13','27','2','22','23','24','25']
x = winning_hand(mains)
for i in range(nb_joueurs+1):
    if i == 0:
        print("Les cartes du milieu")
        for j in range(5):
            print(deck[mains[i][j]][0], deck[mains[i][j]][1])
    if i != 0:
        print("Cartes Joueurs :", i)
        for j in range(2):
            print(deck[mains[i][j]][0], deck[mains[i][j]][1])

print("La main gagnante est :")
for i in range(2):
    print(deck[x[1][i]][0], deck[x[1][i]][1])
print(x)
print(mains)


'''def main_gagnante():
    for i in range(nb_joueurs):
        hand = 
'''
#game_on valeur qui dit qu'on joue un main de poker
'''
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
'''





#Pour inedxer dans deck et afficher les cartes
'''for i in range(5):
    print(deck[mains[0][i]])
for i in range(2):
    print(deck[mains[1][i]])'''

