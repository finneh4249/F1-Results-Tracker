# F1 Results Tracker

[![F1 Results Tracker](https://img.shields.io/badge/F1%20Results%20Tracker-blue)](https://github.com/finneh4249/t1a3-terminal-application)

## Overview

A terminal application that allows users to view and track Formula 1 race results. It interacts with the filesystem to store and retrieve data.

## Features

- **Race Selection**: Select a specific race from a predefined list of races (2021 - 2024 seasons)
- **Results Viewing**: Display race results from a predefined list of races (2021 - 2024 seasons)
- **Driver Tracking**: Track the performance of specific drivers over time based on race results.
- **Filesystem Interaction**: Save and load race data from files for persistent storage.
- **Simple Commands**: Use text-based commands for navigation and interaction.
- **Data Export**: Export tracked data to a file in a simple format like CSV or JSON.

## Scope

- Focus on displaying and tracking race results without simulating the actual racing.
- Implement basic filesystem operations to manage data persistence.
- Keep the user interface minimalistic with clear instructions for use.

## Dependencies

- Python 3.9
- SQLite 3
- Colorama
- Pyfiglet
- Tabulate

## Credits

- [F1DB](https://github.com/f1db/f1db) - F1 Driver Database Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
