import sqlite3
database = "./structures/db/f1db.db"

def get_standings_by_year(table, year):
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
            
            # Determine the column name based on the table name
            if "driver" in table:
                col = "driver_id"
            else:
                col = "constructor_id"
            
            # Execute the query to retrieve the standings
            query = f'SELECT position_display_order, {col}, points FROM {table} WHERE year = {year}'
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
            rows = cur.execute(f'SELECT round, official_name FROM race WHERE year = {year}').fetchall()
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
