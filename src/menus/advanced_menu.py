from structures import app_structures
from menus import main_menu as menu
from .advanced import standings_after_race, top_ten
from colorama import Fore
from tabulate import tabulate
green = Fore.GREEN

class AdvancedMenu(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("View Standings After a Race", standings_after_race.Menu),
            "2": ("View All-Time Records", top_ten.Menu),
            "3": ("Go Back", self.go_back),
        }
    def display_menu(self):
        print(Fore.RED + "Advanced Menu")
        print("Choose a category: \n")  # Display menu options
        for key, value in self.options.items():
            print(Fore.GREEN + f"{key}. {value[0]}")

    def get_user_choice(self):
        return super().get_user_choice()
    
    def call_menu(self, choice):
        self.options[choice][1]().run()

    def go_back(self):
        menu.F1Menu().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)