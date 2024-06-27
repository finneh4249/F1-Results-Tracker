# Import necessary modules from the structures package
from structures import app_structures

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
app_structures.menu()
