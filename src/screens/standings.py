from textual.screen import Screen
from textual.widgets import Header, Footer, Button

class Menu(Screen):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle Dark Mode"),
        ("q", "exit", "Exit"),
    ]

    def on_mount(self):
        self.title = "F1 Results Tracker"
        self.subtitle = "Standings"

    def compose(self):
        yield Button("View Driver Standings", id="driver")
        yield Button("View Constructor Standings", id="constructor")
        yield Button("Back", id="back")

    def action_toggle_dark_mode(self):
        self.dark = not self.dark

    def action_exit(self):
        self.app.exit()

    def view_standings(self, type):
        pass