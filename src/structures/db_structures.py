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
        
