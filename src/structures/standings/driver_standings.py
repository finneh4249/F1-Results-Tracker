from structures import db_structures
from colorama import Fore, Back
from tabulate import tabulate
green = Fore.GREEN

def menu(ascii_title):
    print(green + "Choose a year 1950 - 2024: \n")
    choice = input()
    head = ["Position", "Driver", "Points"]
    if choice == "exit":
        exit()
        
    if int(choice) < 1950 or int(choice) > 2024:
        print(Back.RED + "Invalid choice")
        menu(ascii_title)
        
    print(green + ascii_title(f"{choice} Driver Standings"))
    
    
    
    try:
        standings = db_structures.get_standings_by_year("season_driver_standing", int(choice))
        print(tabulate(standings, headers=head, tablefmt="fancy_grid"))
        menu(ascii_title)
    except:
        print(Back.RED + "Invalid choice")
        menu(ascii_title)
    