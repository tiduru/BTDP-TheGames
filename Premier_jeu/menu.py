import pygame
import pygame_menu

pygame.init()
WINDOW_SIZE=(950,950)
surface=pygame.display.set_mode(WINDOW_SIZE)
Construction="Under Construction ! Be patient"

def main_background():
    background_image(surface)

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass


def reglement1():
    PATH = 'Images\Reglements\CarteHaute.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("CARTE HAUTE", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1,1))
    CarteHaute = "Nommé High Card en anglais, cette combinaison est obtenu si aucune autre combinaison est possible. Tu devrais probablement te coucher (DANS LE JEU VA PAS DODO ON T'AIMES ![à l'exception de Gab])"
    menu.add_label(CarteHaute, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)


def reglement2():
    PATH = 'Images\Reglements\Paire.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("PAIRE", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    Paire = "Nommé Pair en anglais, cette combinaison est obtenu lorsque deux cartes de valeurs identiques, par exemple As-As sont dans la main du joueur."
    menu.add_label(Paire, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement3():
    PATH = 'Images\Reglements\DoublePaire.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("DOUBLE PAIRE", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    DoublePaire = "Nommé Two Pair en anglais, cette combinaison est obtenu si et seulement si le joueur a deux, OUI OUI DEUX !, paires dans sa main."
    menu.add_label(DoublePaire, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement4():
    PATH = 'Images\Reglements\Triple.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("BRELAN", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    Triple = "Nommé Three of a kind en anglais, st'un triple esti de cave"
    menu.add_label(Triple, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement5():
    PATH = 'Images\Reglements\Staright.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("QUINTE", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    straigth1 = "Haha It's Mr. 305 checkin' in for the remix"
    straigth2 = "You know that S 75 Street Brazil?"
    straigth3 = "Well this year it's gon be called Calle Ocho"
    straigth4 = "Hahahaha"
    straigth5 = "Que ola cata, Que ola omega"
    straigth6 = "And this how we gon do it"
    straigth7 = "Dale"
    straigth8 = "One-two-three-four-[five]"
    straigth9 = "Uno-do'-tres-cuatro-[cinqo]"
    straigth0 = "Une suite de chiffre ! Un As peut suivre un roi "
    menu.add_label(straigth1, max_char=-1, fontsize=30)
    menu.add_label(straigth2, max_char=-1, fontsize=30)
    menu.add_label(straigth3, max_char=-1, fontsize=30)
    menu.add_label(straigth4, max_char=-1, fontsize=30)
    menu.add_label(straigth5, max_char=-1, fontsize=30)
    menu.add_label(straigth6, max_char=-1, fontsize=30)
    menu.add_label(straigth7, max_char=-1, fontsize=30)
    menu.add_label(straigth8, max_char=-1, fontsize=30)
    menu.add_label(straigth9, max_char=-1, fontsize=30)
    menu.add_label(straigth0, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement6():
    PATH = 'Images\Reglements\Flush.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("COULEUR", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    Flush1 = "C'est flush en caniche comme qui dise ! "
    Flush2 = "Que tu sois daltonien ou non, faut que tes cartes soit de la même couleur !"
    Flush3 = "Si plus qu'un joueur à ceci, celui avec la carte la plus haute remporte la main"
    menu.add_label(Flush1, max_char=-1, fontsize=30)
    menu.add_label(Flush2, max_char=-1, fontsize=30)
    menu.add_label(Flush3, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement7():
    PATH = 'Images\Reglements\FullHouse.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("FULL", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    FullHouse = "LA MAISON EST PLEINE ! Tu as un triple et un double ! You lucky"
    menu.add_label(FullHouse, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement8():
    PATH = 'Images\Reglements\FourOfAKind.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("CARRÉ", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    quartoo = "uno, dos, tres, quatro : she's a thato ! (non pas un theta) "
    menu.add_label(quartoo, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement9():
    PATH = 'Images\Reglements\StraightFlush.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("QUINTE FLUSH", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    straightNflush= "EN PLUS QUE T'ES CAPABLE DE LIRE CINQ CHIFFRES BACK A BACK SONT TOUS DLA MEME COULEUR ! "
    menu.add_label(straightNflush, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement10():
    PATH = 'Images\Reglements\RoyalFlush.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_label("QUINTE FLUSH ROYALE", max_char=-1, fontsize=40)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    royalflush1 = "Tu es acceuili par les dieux de l'olympe ! TU ES UN DIEU !"
    royalflush2 = "Tu n'as pas beaucoup de couleur différente, un peu raciste, "
    royalflush3 = "mais au moins tu as tous les haut dirigeants du jeu !"
    menu.add_label(royalflush1, max_char=-1, fontsize=30)
    menu.add_label(royalflush2, max_char=-1, fontsize=30)
    menu.add_label(royalflush3, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)


def rules():

    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_button('Carte haute', reglement1)
    menu.add_button('Paire', reglement2)
    menu.add_button('Double paire', reglement3)
    menu.add_button('Triple', reglement4)
    menu.add_button('Suite', reglement5)
    menu.add_button('Flush', reglement6)
    menu.add_button('Full House', reglement7)
    menu.add_button('Carrée', reglement8)
    menu.add_button('Straight Flush', reglement9)
    menu.add_button('Royal Flush', reglement10)

    menu.add_button('Retour', poker_menu)
    menu.mainloop(surface)


def options ():
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Options',
                            theme=pygame_menu.themes.THEME_DARK)
    menu.add_label(Construction, max_char=-1, font_size=30)
    menu.add_button('Retour', main_menu)
    menu.mainloop(surface)

def main_menu():
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Jeu pour jouer entre amis !',
                           theme=pygame_menu.themes.THEME_ORANGE)


    menu.add_selector('Jeu à jouer :', [('Poker', 1)], onchange=set_difficulty)
    menu.add_button('Jouer', poker_menu)
    menu.add_button('Options', options)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(surface)

def poker_menu():
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Poker',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_text_input('Name :', default='Dumbass')
    menu.add_button('Rejoindre une party', start_the_game)
    menu.add_button('Règle de jeu', rules)
    menu.add_button('Retour', main_menu)

    menu.mainloop(surface)
#Main Loop

def main():
    main_menu()

main()