import os
from time import sleep
import pyfiglet
from colorama import Fore


def title_art(t):
    return pyfiglet.figlet_format(t, font="smslant")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def load(sec):
    sleep(sec)


class BaseMenu:
    """
    Base class for all menus in the app.
    """

    def __init__(self):
        pass

    def display_menu(self):
        """
        Display the menu options.
        """
        raise NotImplementedError

    def get_user_choice(self):
        """
        Get user's choice.
        """
        return input()

    def call_menu(self, choice):
        """
        Call the respective menu function based on the user's choice.
        """
        raise NotImplementedError


def exit_program():
    print(Fore.RED + "Exiting...")
    sleep(1)
    clear()
    exit()

def check_for_updates():
    print(Fore.RED + "Checking for updates...")
    sleep(1)
    
    import requests
    import os
    
    # Check the F1DB Repository for a new release
    response = requests.get('https://api.github.com/repos/f1db/f1db/releases/latest')
    release_data = response.json()
    latest_version = release_data['tag_name']

    import sqlite3
    conn = sqlite3.connect("./structures/db/history.db")
    cursor = conn.cursor()
    cursor.execute(
                f"CREATE TABLE IF NOT EXISTS versions (version TEXT)")
    conn.commit()
    
    cursor.execute("SELECT version FROM versions LIMIT 1")
    current_version = cursor.fetchone()
    if current_version is not None:
        current_version = current_version[0]
    # If the version is none, insert the latest version
    if current_version is None:
        cursor.execute("INSERT INTO versions VALUES (?)", (latest_version,))
    elif latest_version == current_version:
        print("You are already on the latest version.")
        sleep(1)
        return
    else:
        cursor.execute("UPDATE versions SET version = ?", (latest_version,))
    conn.commit()

    conn.close()

    
    print(Fore.RED + "Updating...")
    f1db_download_url = release_data['assets'][9]['browser_download_url']

    # Download the latest version of the SQLite database (f1db.sqlite.zip)
    response = requests.get(f1db_download_url, stream=True)
    with open('f1db.sqlite.zip', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    
    import zipfile

    # Extract the downloaded zip file to the ./db folder
    with zipfile.ZipFile('f1db.sqlite.zip', 'r') as zip_ref:
        zip_ref.extractall('./structures/db')

    # Remove the downloaded zip file
    os.remove('f1db.sqlite.zip')

    print(Fore.RED + "Updated F1DB to version " + latest_version)
    sleep(1)

    # Restart the app
    print(Fore.RED + "Restarting...")
    sleep(1)
    clear()