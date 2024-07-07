from structures import app_structures, db_structures, db_store_history
from menus import advanced_menu as menu
from colorama import Fore, Back
from tabulate import tabulate
green = Fore.GREEN


class Menu(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("View Driver Standings", self.view_standings),
            "2": ("View Constructor Standings", self.view_standings),
            "3": ("Go Back", self.go_back),
        }

    def display_menu(self):
        print("Choose a category: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return super().get_user_choice()

    def call_menu(self, choice):
        if choice == "1":
            self.view_standings("driver")
        elif choice == "2":
            self.view_standings("constructor")
        elif choice == "3":
            self.go_back()

    def view_standings(self, type):
        app_structures.clear()

        title = type.title()

        if type == "driver":
            print(green + "Choose a year (1950 - 2024): \n")
            year = input()
            if int(year) < 1950 or int(year) > 2024:
                print(Back.RED + "Invalid choice")
                return self.view_standings(type)

        if type == "constructor":
            print(green + "Choose a year (1958 - 2024): \n")
            year = input()
            if int(year) < 1958 or int(year) > 2024:
                print(Back.RED + "Invalid choice")
                return self.view_standings(type)

        races = db_structures.get_race_id_by_year(int(year))
        race_head = ["Round No.", "Race Name"]
        print(tabulate(races, headers=race_head, tablefmt="fancy_grid"))
        print(green + "Choose a race \n")
        race = input()
        results = db_structures.get_standings_after_race(
            type, int(year), int(race))
        print(Fore.GREEN + "Getting Results...")
        app_structures.load(2)
        results_head = ["Position", f"{title}", "Points", "Positions Gained"]
        for r in races:
            if str(r[0]) == race:
                race_name = r[1]
                app_structures.clear()
                print(
                    green + app_structures.title_art(f"{title} Standings after {race_name}"))
                break
        print(tabulate(results, headers=results_head, tablefmt="fancy_grid"))
        db_store_history.add_search(f"{title} Standings after {race_name}")

    def go_back(self):
        menu.AdvancedMenu().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)
