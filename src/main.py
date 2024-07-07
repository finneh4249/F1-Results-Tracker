from structures import app_structures
# Import necessary modules from the structures package
from menus import main_menu, help_menu, advanced_menu
from sys import argv
# Import colours from colorama
from colorama import Fore, Back, init
from time import sleep

# Initialise colorama
init(autoreset=True)

# Define colous
red = Fore.RED
green = Fore.GREEN

# Check if the user has entered any arguments
# Arguments we use:
#    -h or --help - display help
#    -v or --version - display version
#    -a or --advanced - display advanced options
#    -s or --simple - display simple options

app_structures.clear()

# Display ASCII art title
title = app_structures.title_art("F1 Results Tracker")
print(red + title)

if len(argv) > 1:
    if argv[1] == "-h" or argv[1] == "--help":
        help_menu.HelpMenu().run()
    elif argv[1] == "-v" or argv[1] == "--version":
        print("Version 1.0.0")
        exit()
    elif argv[1] == "-a" or argv[1] == "--advanced":
        advanced_menu.AdvancedMenu().run()
        print("Advanced options")
    elif argv[1] == "-s" or argv[1] == "--simple":
        main_menu.F1Menu().run()
        print("Simple options")
# If no arguments are entered, display the main menu
else:
    main_menu.F1Menu().run()








