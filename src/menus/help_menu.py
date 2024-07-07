from menus import main_menu as menu
from structures import app_structures
from colorama import Fore


class HelpMenu(app_structures.BaseMenu):
    def __init__(self):
        self.options = {
            "menu": ("Main Menu", menu.F1Menu),
        }

    def display_menu(self):
        with open("structures/help.txt", "r") as f:
            help_text = f.read()
        print(help_text)
        print(Fore.RED + "Type 'menu' to return to the main menu.")

    def get_user_choice(self):
        return super().get_user_choice()

    def call_menu(self, choice):
        self.options[choice][1]().run()

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            if choice in self.options:
                self.call_menu(choice)
