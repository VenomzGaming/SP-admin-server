## IMPORTS

from .mysql import MySQL
from .sqlite import SQLite

## ALL DECLARATION

__all__ = (
    'manager',
)


## DATABASE CHOICE

DATABASE_TYPE = 1

if DATABASE_TYPE == 1:
    manager = SQLite()
elif DATABASE_TYPE == 2:
    manager = MySQL()
else:
    # TODO : Add log message
    manager = SQLite()
