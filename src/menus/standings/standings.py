from structures import db_structures, app_structures, db_store_history
from menus import main_menu as menu
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
        try:
            if type == "driver":
                print(green + "Choose a year 1950 - 2024: \n")
                choice = input()
                if int(choice) < 1950 or int(choice) > 2024:
                    print(Back.RED + "Invalid choice")
                    app_structures.load(1)

                    return self.view_standings(type)

            if type == "constructor":
                print(green + "Choose a year 1958 - 2024: \n")
                choice = input()
                if int(choice) < 1958 or int(choice) > 2024:
                    print(Back.RED + "Invalid choice")
                    app_structures.load(1)

                    return self.view_standings(type)
        except ValueError:
            print(Back.RED + "Invalid choice")
            app_structures.load(1)

            return self.view_standings(type)

        head = ["Position", f"{title}", "Points"]

        try:
            standings = db_structures.get_standings_by_year(
                f"season_{type}_standing", int(choice), type)
            app_structures.clear()
            print(Fore.GREEN + "Getting Results...")
            app_structures.load(2)
            app_structures.clear()
            print(
                green + app_structures.title_art(f"{choice} {title} Standings"))
            print(tabulate(standings, headers=head, tablefmt="fancy_grid"))
            db_store_history.add_search(f"{choice} {title} Standings")
        except:
            print(Back.RED + "Invalid choice")
            app_structures.load(1)

    def go_back(self):
        menu.F1Menu().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)
            else:
                # Display error message for invalid choice
                print(Back.RED + "Invalid choice")
                app_structures.load(1)
