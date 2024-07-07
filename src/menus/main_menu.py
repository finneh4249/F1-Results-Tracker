from structures import app_structures as app
from .standings import driver_standings, constructor_standings, race_results
from menus import help_menu
from colorama import Fore, Back


class F1Menu(app.BaseMenu):
    """
    This class displays a menu of options to the user and calls the respective
    standings and race results menus based on the user's choice.
    """

    def __init__(self):
        self.options = {
            "1": ("Driver Standings", driver_standings.menu),
            "2": ("Team Standings", constructor_standings.menu),
            "3": ("Race Results", race_results.RaceResults.display_menu(self)),
            "4": ("Help", ),
            "5": ("Exit", exit)
        }

    def display_menu(self):
        print("Choose a category: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return input()

    def call_menu_function(self, choice):
        self.options[choice][1](app.ascii_title)

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu_function(choice)
            else:
                print(Back.RED + "Invalid choice")  # Display error message for invalid choice
            