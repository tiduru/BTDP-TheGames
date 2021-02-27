import pygame
import pygame_menu

pygame.init()
WINDOW_SIZE=(600,600)
surface=pygame.display.set_mode(WINDOW_SIZE)
def main_background():
    background_image(surface)
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

def rules():
    pass

def options ():
    pass

def main_menu():
    menu = pygame_menu.Menu(600, 600, 'Ah bin caliss',
                           theme=pygame_menu.themes.THEME_ORANGE)


    menu.add_selector('Jeu à jouer :', [('Poker', 1)], onchange=set_difficulty)
    menu.add_button('Jouer', poker_menu)
    menu.add_button('Options', options)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(surface)

def poker_menu():
    menu = pygame_menu.Menu(600, 600, 'Poker',
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add_text_input('Name :', default='Blow Me Daddy')
    menu.add_button('Rejoindre une party', start_the_game)
    menu.add_button('Règle de jeu', rules)
    menu.add_button('Retour', main_menu)

    menu.mainloop(surface)
#Main Loop

def main():
    main_menu()

main()