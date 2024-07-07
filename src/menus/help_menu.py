from menus import main_menu as menu
from colorama import Fore
def help_menu():
    """
    This function reads the help.txt file and displays the content to the user.
    """
    with open("structures/help.txt", "r") as f:
        help_text = f.read()
    print(help_text)
    print(Fore.RED + "Type 'menu' to return to the main menu.")
    
    if input() == "menu":
        menu()
    else:
        help_menu() 