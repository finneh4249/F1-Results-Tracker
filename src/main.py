from structures import app_structures
# Import necessary modules from the structures package
from menus import main_menu as menu

# Import colours from colorama
from colorama import Fore, Back, init

# Initialise colorama
init(autoreset=True)

# Define colous
red = Fore.RED
green = Fore.GREEN

# Display ASCII art title
title = app_structures.ascii_title("F1 Results Tracker")
print(red + title)

# Call the main menu function
menu.F1Menu().run()
