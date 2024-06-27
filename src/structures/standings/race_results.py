from structures import db_structures
from colorama import Fore, Back
from tabulate import tabulate
green = Fore.GREEN

def menu(ascii_title):
    print(green + "Choose a year (1950 - 2024): \n")
    year = input()
    
    if int(year) < 1950 or int(year) > 2024:
        print(Back.RED + "Invalid choice")
        return menu(ascii_title)
    
    races = db_structures.get_race_id_by_year(int(year))
    race_head = ["Round No.", "Race Name"]
    print (tabulate(races, headers= race_head, tablefmt="fancy_grid"))
    print(green + "Choose a race \n")
    race = input()
    results = db_structures.get_race_results(int(year), int(race))
    results_head = ["Position", "Driver", "Constructor", "Gap to Leader", "Points", "Grid Position", "Positions Gained"]
    for r in races:
        if str(r[0]) == race:
            race_name = r[1]
            print(green + ascii_title(f"{race_name} Race Results"))
            break
    print(tabulate(results, headers= results_head, tablefmt="fancy_grid"))
    menu(ascii_title)
    
    