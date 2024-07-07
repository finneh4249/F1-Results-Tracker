from structures import app_structures, db_structures, db_store_history
from menus import advanced_menu as menu
from colorama import Fore, Back
from tabulate import tabulate
green = Fore.GREEN


class Menu(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("View Driver Records", view_records),
            "2": ("View Constructor Records", view_records),
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
            type = "driver"
        elif choice == "2":
            type = "constructor"
        self.options[choice][1](type)

    def go_back(self, type):
        menu.AdvancedMenu().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)


def view_results(type, title):
    app_structures.clear()

    results = db_structures.get_topten_results(type, f"total_{title.lower()}")
    print(green + "Getting Results...")

    app_structures.load(2)

    display_results(results, title, type)


def display_results(results, title, type):
    app_structures.clear()
    display_title = title.replace("_", " ").title()
    print(green + app_structures.title_art(f"Top 10 {display_title}"))
    head = [type.title(), display_title]
    print(tabulate(results, headers=head, tablefmt="fancy_grid"))
    app_structures.load(3)
    db_store_history.add_search(f"Top 10 {title} - {type}")


def view_records(type):

    options = {
        "1": ("View Top 10 Pole Positions", view_results),
        "2": ("View Top 10 Fastest Lap", view_results),
        "3": ("View Top 10 Champions", view_results),
        "4": ("View Top 10 Podiums", view_results),
        "5": ("View Top 10 Points", view_results),
        "6": ("View Top 10 Wins", view_results),
        "7": ("Go Back", Menu.go_back),
    }
    print("Choose a category: \n")
    for key, value in options.items():
        print(green + f"{key}. {value[0]}")
    choice = input()
    if choice not in options:
        print(Back.RED + "Invalid choice")
        return view_records(type)

    if choice == "1":
        title = "pole_positions"
    elif choice == "2":
        title = "fastest_laps"
    elif choice == "3":
        title = "championship_wins"
    elif choice == "4":
        title = "podiums"
    elif choice == "5":
        title = "championship_points"
    elif choice == "6":
        title = "wins"

    return options[choice][1](type, title)
