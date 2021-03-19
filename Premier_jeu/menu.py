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
    menu.add_image(PATH, angle=0, scale=(1,1))
    CarteHaute = "Nommé High Card en anglais, cette combinaison est obtenu si aucune autre combinaison est possible. Tu devrais probablement te coucher (DANS LE JEU VA PAS DODO ON T'AIMES ![à l'exception de Gab])"
    menu.add_label(CarteHaute, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)


def reglement2():
    PATH = 'Images\Reglements\Paire.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    Paire = "Nommé Pair en anglais, cette combinaison est obtenu lorsque deux cartes de valeurs identiques, par exemple As-As sont dans la main du joueur."
    menu.add_label(Paire, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement3():
    PATH = 'Images\Reglements\DoublePaire.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    DoublePaire = "Nommé Two Pair en anglais, cette combinaison est obtenu si et seulement si le joueur a deux, OUI OUI DEUX !, paires dans sa main."
    menu.add_label(DoublePaire, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement4():
    PATH = 'Images\Reglements\Triple.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    Triple = "Nommé Three of a kind en anglais, st'un triple esti de cave"
    menu.add_label(Triple, max_char=-1, fontsize=30)
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement5():
    PATH = 'Images\Reglements\Staright.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement6():
    PATH = 'Images\Reglements\Flush.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement7():
    PATH = 'Images\Reglements\FullHouse.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement8():
    PATH = 'Images\Reglements\FourOfAKind.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement9():
    PATH = 'Images\Reglements\StraightFlush.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
    menu.add_button('Retour', rules)
    menu.mainloop(surface)

def reglement10():
    PATH = 'Images\Reglements\RoyalFlush.PNG'
    menu = pygame_menu.Menu(WINDOW_SIZE[0], WINDOW_SIZE[1], 'Règlements',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_image(PATH, angle=0, scale=(1, 1))
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
    menu.add_text_input('Name :', default='Joe Mama')
    menu.add_button('Rejoindre une party', start_the_game)
    menu.add_button('Règle de jeu', rules)
    menu.add_button('Retour', main_menu)

    menu.mainloop(surface)
#Main Loop

def main():
    main_menu()

main()