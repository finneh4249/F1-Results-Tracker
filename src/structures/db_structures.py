import sqlite3
database = "./structures/db/f1db.db"


def get_standings_by_year(table, year, type):
    """
    Retrieves the position display order, driver/constructor ID, and points for a specific year.

    Args:
        table (str): The name of the table in the database.
        year (int): The year of the standings.

    Returns:
        List[List[str]]: A list of standings, each containing the position display order,
        driver/constructor ID, and points.
    """
    try:
        # Connect to the database
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()

            # Execute the query to retrieve the standings
            query = f'SELECT position_display_order, {
                type}_id, points FROM {table} WHERE year = {year}'
            rows = cur.execute(query).fetchall()

            # Format the results
            rows = [[i[0], i[1].replace("-", " ").title(), i[2]] for i in rows]

            return rows

    # Print the error message if there is any error in the database operation
    except sqlite3.Error as e:
        print(e)


def get_race_id_by_year(year):
    """
    Retrieves the round and official name of races for a specific year.

    Args:
        year (int): The year of the race.

    Returns:
        List[List[str]]: A list of race details, each containing the round and official name.
    """
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            # Query the database to get the round and official name of races for a specific year
            rows = cur.execute(f'SELECT round, official_name FROM race WHERE year = {
                               year}').fetchall()
            return rows
    except sqlite3.Error as e:
        # Print the error message if there is any error in the database operation
        print(e)


def get_race_results(year, round):
    """
    Returns race results for a specific year and round.

    Args:
        year (int): The year of the race.
        round (int): The round number of the race.

    Returns:
        List[List[str]]: A list of race results, each containing the position text,
        driver name, constructor name, race gap, race points, race grid position,
        and race positions gained.
    """
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            # Get the id of the race
            id = cur.execute(
                f'SELECT id FROM race WHERE year = {year} AND round = {round}'
            ).fetchone()[0]
            # Get the race results
            results = cur.execute(
                f'SELECT position_text,driver_id, constructor_id, race_gap, '
                f'race_points, race_grid_position_number, race_positions_gained '
                f'FROM race_data WHERE race_id = {id} AND type = "RACE_RESULT"'
            ).fetchall()
            # Format the results
            results = [
                [
                    i[0],
                    i[1].replace("-", " ").title(),
                    i[2].replace("-", " ").title(),
                    i[3],
                    i[4],
                    i[5],
                    i[6],
                ]
                for i in results
            ]
            return results
    except sqlite3.Error as e:
        print(e)


def get_standings_after_race(type, year, round):
    """
    Returns the standings after a race for a specific year and round.

    Args:
        type (str): The type of standings (driver or constructor).
        year (int): The year of the race.
        round (int): The round number of the race.

    Returns:
        List[List[str]]: A list of standings, each containing the position display order,
        driver name, and points.
    """
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            # Get the id of the race
            id = cur.execute(
                f'SELECT id FROM race WHERE year = {year} AND round = {round}'
            ).fetchone()[0]
            # Get the standings after the race
            standings = cur.execute(
                f'SELECT position_display_order, {type}_id, points, positions_gained FROM race_{type}_standing WHERE race_id = {id}').fetchall()\

            # Format the results
            standings = [
                [i[0], i[1].replace("-", " ").title(), i[2], i[3]] for i in standings]
            return standings
    except sqlite3.Error as e:
        print(e)


def get_topten_results(type, option):
    """
    Returns the top ten results for a specific type of event.

    Args:
        type (str): The type of event, either "constructor" or "driver".
        option (str): The option to filter by, either "points" or "positions_gained".

    Returns:
        List[List[str]]: A list of top ten results, each containing the position display order,
        driver name, and points.
    """
    try:
        with sqlite3.connect(database) as conn:
            cur = conn.cursor()
            # Get the top ten results

            # Select the top ten results from driver or constructor table, depending on the option (total_championship_wins, total_championship_points, total_pole_positions, etc)
            results = cur.execute(
                f'SELECT id, {option} FROM {type} WHERE {option} IS NOT NULL ORDER BY {option} DESC LIMIT 10').fetchall()
            # Format the results
            results = [[i[0].replace("-", " ").title(), i[1]] for i in results]
            return results
    except sqlite3.Error as e:
        print(e)
