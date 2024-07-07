import pyfiglet
from colorama import Fore
def title_art(t):
    return pyfiglet.figlet_format(t, font="smslant")

import os
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load(sec):
    sleep(sec)

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
        return input()

    def call_menu(self, choice):
        """
        Call the respective menu function based on the user's choice.
        """
        raise NotImplementedError



def exit_program():
    print(Fore.RED + "Exiting...")
    sleep(1)
    clear()
    exit()


