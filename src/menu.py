import pygame_menu
import pygame
from global_vars import GlobalVars


class Menu:

    def __init__(self, start_game_callback, quit_game_callback):
        self.menu = pygame_menu.Menu(
            int(GlobalVars.get_screen_size().x * 0.6),
            int(GlobalVars.get_screen_size().y * 0.6), 
            'Floppy Birdie',         
            theme=pygame_menu.themes.THEME_BLUE)


        self.menu.add_button("Start", start_game_callback)
        self.menu.add_button("Quit", quit_game_callback)