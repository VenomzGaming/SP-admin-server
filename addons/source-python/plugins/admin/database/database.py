## IMPORTS

## ALL DECLARATION

__all__ = (
    '_Database',
)

class _Database:
    ''' Class Wrapper for Sql management '''

    def execute(self, statement, *args):
        if not isinstance(statement, str):
            raise TypeError('<{}>.execute requires a string statement.'.format(self.__class__.__name__))

        self.cursor.execute(statement, *args)

    def create_tables(self):
        pass
