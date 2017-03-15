## IMPORTS

from sqlite3 import connect

# TODO : Config for sqlite location
# from ..config import SQLITE_LOCATION

## ALL DECLARATION

__all__ = (
    'SQLite',
    ) 

SQLITE_LOCATION = None

class SQLite:
    ''' SQLite database manager '''

    def __init__(self, location=SQLITE_LOCATION):
        self.connection = connect(location)
        self.cursor = self.connection.cursor()
