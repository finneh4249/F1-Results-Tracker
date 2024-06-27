from colorama import Fore, Back

from .standings import driver_standings, constructor_standings, race_results
red = Fore.RED
green = Fore.GREEN

import pyfiglet

def ascii_title(t):
    return pyfiglet.figlet_format(t, font="slant")

def menu():
    """
    This function displays a menu of options to the user and calls the respective
    standings and race results menus based on the user's choice.
    """
    print("Choose a category: \n")  # Display menu options
    print(green + "1. Driver Standings")
    print(green + "2. Team Standings")
    print(green + "3. Race Results")
    print(green + "4. Exit")
    
    choice = input()  # Get user's choice
    
    # Match the user's choice and call the respective menu
    match choice:
        case "1":
            title = ascii_title("Driver Standings")  # Display ASCII art title
            print(red + title)
            driver_standings.menu(ascii_title)
        case "2":
            title = ascii_title("Team Standings")
            print(red + title)
            constructor_standings.menu(ascii_title)
        case "3":
            title = ascii_title("Race Results")
            print(red + title)
            race_results.menu(ascii_title)
            menu()  # Call menu again after race results are displayed
        case "4":
            print(red + "Goodbye!")  # Display exit message
            exit()
        case _:
            print(Back.RED + "Invalid choice")  # Display error message for invalid choice
            menu()
            

