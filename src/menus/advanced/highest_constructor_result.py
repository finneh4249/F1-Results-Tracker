from structures import app_structures, db_structures
from menus import advanced_menu as menu
from colorama import Fore, Back
from tabulate import tabulate
green = Fore.GREEN

class Menu(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("View Top 10 Pole Positions", self.view_poles),
            "2": ("View Top 10 Fastest Lap", self.view_fastest_lap),
            "3": ("View Top 10 Champions", self.view_champs),
            "4": ("View Top 10 Podiums", self.view_podiums),
            "5": ("View Top 10 Points", self.view_points),
            "6": ("View Top 10 Wins", self.view_wins),
            "7": ("Go Back", self.go_back),
        }
    def display_menu(self):
        print("Choose a category: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return super().get_user_choice()
    
    def call_menu(self, choice):
        self.options[choice][1]()

    def go_back(self):
        menu.AdvancedMenu().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)
    

    def view_poles(self):
        app_structures.clear()

        results = db_structures.get_topten_results("constructor", "total_pole_positions")
        print(green + "Getting Results...")

        app_structures.load(2)

        display_results(results, "Poles")

    def view_fastest_lap(self):
        app_structures.clear()

        results = db_structures.get_topten_results("constructor", "total_fastest_laps")
        print(green + "Getting Results...")

        app_structures.load(2)

        display_results(results, "Fastest Laps")

    def view_champs(self):
        app_structures.clear()

        results = db_structures.get_topten_results("constructor", "total_championship_wins")
        print(green + "Getting Results...")

        app_structures.load(2)

        display_results(results, "Championships")

    def view_podiums(self):
        app_structures.clear()

        results = db_structures.get_topten_results("constructor", "total_podiums")
        print(green + "Getting Results...")

        app_structures.load(2)

        display_results(results, "Podiums")

    def view_points(self):
        app_structures.clear()

        results = db_structures.get_topten_results("constructor", "total_championship_points")
        print(green + "Getting Results...")

        app_structures.load(2)

        display_results(results, "Points")

    def view_wins(self):
        app_structures.clear()

        results = db_structures.get_topten_results("constructor", "total_race_wins")
        print(green + "Getting Results...")

        app_structures.load(2)

        display_results(results, "Race Wins")

def display_results(results, title):
    app_structures.clear()
    print(green + app_structures.title_art(f"Top 10 {title}"))
    print(tabulate(results, headers=["Constructor", f"{title}"], tablefmt="fancy_grid"))
    db_store_history.add_search(f"Top 10 {title} - Constructor")
    app_structures.load(3)
