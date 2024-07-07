from menus.standings import driver_standings

import pytest

@pytest.mark.parametrize("year", range(1950, 2025))
def test_driver_standings(year):
    standings = driver_standings.DriverStandings().view_driver_standings(year)
    assert isinstance(standings, list)
    assert all(isinstance(item, list) for item in standings)
    assert all(len(item) == 3 for item in standings)
