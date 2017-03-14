## IMPORTS

from pymysql import connect

from ..config import MYSQL_ADDRESS
from ..config import MYSQL_PORT
from ..config import MYSQL_LOGIN
from ..config import MYSQL_PASSWORD
from ..config import MYSQL_DATABASE_NAME
from .sqlite import SQLite

## ALL DECLARATION

__all__ = (
    'MySQL',
    )

## 

class MySQL(SQLite):
    '''

    MySQL database manager. Loads
    data into <Player> instances, and
    saves data from <Player> instances
    to the database.

    '''

    def __init__(self, host=MYSQL_ADDRESS, port=MYSQL_PORT, user=MYSQL_LOGIN, pw=MYSQL_PASSWORD, db=MYSQL_DATABASE_NAME):
        self.connection = connect(host=host, port=port, user=user, password=pw, db=db)
        self.cursor = self.connection.cursor()
