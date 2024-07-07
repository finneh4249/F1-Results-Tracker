# F1 Results Tracker

[![F1 Results Tracker](https://img.shields.io/badge/F1%20Results%20Tracker-blue)](https://github.com/finneh4249/t1a3-terminal-application)

## Overview

A terminal application that allows users to view and track Formula 1 race results. It interacts with an SQLIte to store and retrieve data.

## Features

### Driver & Constructor Standings
View the drivers and constructors standing for any year of the Formula 1 Championship.
> NOTE: Constructors Standings are only available for years 1958 - 2024 as there was not a Constructors Championship before that.

### Race Results
View the race results for any year, and any race of the Formula 1 Championship.

### Standings After Race (Advanced Feature)
View the standings after the race for any year of the Formula 1 Championship.
> NOTE: Constructor Standings After Race is only available for years 1958 - 2024 as there was not a Constructors Championship before that.

### Top 10 Results (Advanced Feature)
View the top 10 results for different records.

- Top 10 Pole Positions
- Top 10 Fastest Lap
- Top 10 Championship
- Top 10 Podiums
- Top 10 Points
- Top 10 Wins

### Search Results

Each search is stored in an SQLite database, and can be accessed from the main menu by selecting "View History"

## Scope

- Focus on displaying race results without simulating the actual racing.
- Implement an SQLIte database to store and retrieve data.
- Keep the user interface minimalistic with clear instructions for use.

## Dependencies

- Python 3.9
- SQLite 3
- Colorama
- Pyfiglet
- Tabulate

## Installation

The first time you run the application you must first install the required dependencies.
To do this you can run the `install.sh` script.

- Ensure that you're inside the `src` directory using `cd src`
- Run the script using
```bash
./install.sh
```

## Usage

To start the app, simply run the `./run.sh` script in the `src` directory.

### Arguments

There are also arguments that can be passed to the script to change the behaviour of the application.

- `-h` or `--help` - Display a help message
- `-v` or `--version` - Display the application version
- `-a` or `--advanced` - Display the advanced menu
- `-s` or `--simple` - Display the simple menu

## Credits

- [F1DB](https://github.com/f1db/f1db) - F1 Driver Database Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
