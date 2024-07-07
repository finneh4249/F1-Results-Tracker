from colorama import Fore, Back

red = Fore.RED
green = Fore.GREEN

import pyfiglet

def ascii_title(t):
    return pyfiglet.figlet_format(t, font="smslant")



class BaseMenu:
    """
    Base class for all menus in the app.
    """

    def __init__(self):
        pass

    def display_menu(self):
        """
        Display the menu options.
        """
        raise NotImplementedError

    def get_user_choice(self):
        """
        Get user's choice.
        """
        raise NotImplementedError

    def call_menu_function(self, choice):
        """
        Call the respective menu function based on the user's choice.
        """
        raise NotImplementedError




