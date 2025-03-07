from structures import app_structures as app
from .standings import race_results, standings
from menus import help_menu, advanced_menu
from structures import db_store_history
from colorama import Fore, Back
from tabulate import tabulate


class F1Menu(app.BaseMenu):
    """
    This class displays a menu of options to the user and calls the respective
    standings and race results menus based on the user's choice.
    """

    def __init__(self):
        self.options = {
            "1": ("View Standings", standings.Menu),
            "2": ("View Race Results", race_results.RaceResults),
            "3": ("Advanced Menu", advanced_menu.AdvancedMenu),
            "4": ("Help", help_menu.HelpMenu),
            "5": ("View History", view_history),
            "6": ("Exit", app.exit_program),
        }

    def display_menu(self):

        print(Fore.RED + app.title_art("F1 Results Tracker"))
        print("Choose a category: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return super().get_user_choice()

    def call_menu(self, choice):
        self.options[choice][1]().run()

    def run(self):
        while True:
            app.clear()
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)
            else:
                # Display error message for invalid choice
                print(Back.RED + "Invalid choice")


def view_history():
    print(Fore.RED + "Viewing history...")
    results = db_store_history.get_searches()
    app.load(1)
    print(tabulate(results, headers=["Search", "Time"], tablefmt="fancy_grid"))
    HistoryMenu().run()


class HistoryMenu(app.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("Go Back", self.go_back),
        }

    def display_menu(self):
        print("Choose an option: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return super().get_user_choice()

    def call_menu(self, choice):
        if choice == "1":
            self.go_back()

    def go_back(self):
        F1Menu().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)
            else:
                # Display error message for invalid choice
                print(Back.RED + "Invalid choice")
                app.load(1)
