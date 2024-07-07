from structures import app_structures as app
from .standings import driver_standings, constructor_standings, race_results
from menus import help_menu, advanced_menu
from colorama import Fore, Back


class F1Menu(app.BaseMenu):
    """
    This class displays a menu of options to the user and calls the respective
    standings and race results menus based on the user's choice.
    """

    def __init__(self):
        self.options = {
            "1": ("Driver Standings", driver_standings.DriverStandings),
            "2": ("Team Standings", constructor_standings.ConstructorStandings),
            "3": ("Race Results", race_results.RaceResults),
            "4": ("Help", help_menu.HelpMenu),
            "5": ("Exit", exit)
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
                print(Back.RED + "Invalid choice")  # Display error message for invalid choice
            