from structures import app_structures
from menus import main_menu as menu
from .advanced import highest_driver_result, wdc_after_race, highest_constructor_result, wcc_after_race
from colorama import Fore
from tabulate import tabulate
green = Fore.GREEN

class AdvancedMenu(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "1": ("View Driver Standings After a Race", wdc_after_race.Menu),
            "2": ("View Driver Records", highest_driver_result.Menu),
            "3": ("View Constructor Standings After a Race", wcc_after_race.Menu),
            "4": ("View Constructor Records", highest_constructor_result.Menu),
            "5": ("Go Back", self.go_back),
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
        menu.F1Menu.run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)