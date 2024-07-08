from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Container, Grid
from textual.widgets import Header, Footer, Button, Static, Label
from textual import on
import screens
import pyfiglet

class QuitScreen(Screen):
    """Screen with a dialog to quit."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label("Are you sure you want to quit?", id="question"),
            Button("Quit", variant="success", id="quit"),
            Button("Cancel", id="cancel"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "quit":
            self.app.exit()
        else:
            self.app.pop_screen()


class MenuButtons(Static):
    def compose(self):
            yield Button("View Standings", id="view-standings", variant="success" )
            yield Button("View Race Results", id="view-results", variant="success" )
            yield Button("Advanced Menu", id="advanced-menu", variant="success" )
            yield Button("Help", id="help")
            yield Button("History", id="history")
            classes="menu"

    @on(Button.Pressed, "#view-standings")
    def view_standings(self):
        self.app.load("standings")

    @on(Button.Pressed, "#view-results")
    def view_results(self):
        self.app.load(2)

    @on(Button.Pressed, "#advanced-menu")
    def advanced_menu(self):
        self.app.load(3)

    @on(Button.Pressed, "#help")
    def help(self):
        self.app.load(4)

    @on(Button.Pressed, "#history")
    def history(self):
        self.app.load(5)

class MainMenu(Screen):
    def compose(self):
        yield Header(show_clock=True)
        yield Footer()
        yield Label(pyfiglet.figlet_format("F1 Results Tracker"), id="title")
        with Container(classes="menu"):
            yield MenuButtons()
class Standings(Screen):
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
class F1ResultsTracker(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        ("d", "toggle_dark_mode", "Toggle Dark Mode"),
        ("q", "request_quit", "Exit"),
    ]
    SCREENS = {
        "MainMenu": MainMenu(),
        "QuitScreen": QuitScreen(),
    }
    def on_mount(self):
         self.title = "F1 Results Tracker"
         self.push_screen("MainMenu")
         self.install_screen("Standings", screens.Standings.Menu())
    def action_toggle_dark_mode(self):
        self.dark = not self.dark
    
    def action_exit(self):
        self.exit()

    def action_request_quit(self) -> None:
        self.push_screen(QuitScreen())

    def load(self, page):
        self.push_screen(page)



if __name__ == "__main__":
    F1ResultsTracker().run()