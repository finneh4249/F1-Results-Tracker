from structures import db_structures, app_structures
from menus import main_menu as menu
from colorama import Fore, Back
from tabulate import tabulate
green = Fore.GREEN

class ConstructorStandings(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("View Constructor Standings", self.view_constructor_standings),
            "2": ("Go Back", self.go_back),
        }
    def display_menu(self):
        print("Choose a category: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return super().get_user_choice()
    
    def call_menu(self, choice):
        if choice == "1":
            self.view_constructor_standings()
        elif choice == "2":
            self.go_back()

    def view_constructor_standings(self):
        app_structures.clear()
        print(green + "Choose a year 1958 - 2024: \n")
        choice = input()
        head = ["Position", "Constructor", "Points"]
        if int(choice) < 1958 or int(choice) > 2024:
            print(Back.RED + "Invalid choice")
        
        
        try:
            standings = db_structures.get_standings_by_year("season_constructor_standing", int(choice))
            app_structures.clear()
            print(green + app_structures.title_art(f"{choice} Constructor Standings"))
            print(tabulate(standings, headers=head, tablefmt="fancy_grid"))
        except:
            print(Back.RED + "Invalid choice")
    

    def go_back(self):
        menu.F1Menu().run()
    
    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)

