from collections import defaultdict
from inspect import signature

## ALL DECLARATION

__all__ = (
    'command_manager',
)


class CommandManager(defaultdict):
    """This class provides a decorador used to add commands for clients
    You can define a command by doing
    `@command_manager.add_command(<command>, <permission>)` above a function"""
    
    def __missing__(self, item):
        return (None, None)

    def add_command(self, command, permission):
        if command in self:
            raise CommandException('Cannot re-assign command ({command_name})'.format(command_name=command))

        def decorator(method):
            ## Retrieves the functions argument count.
            ## Used to verify the client/say command is valid.
            self[command] = (
                method,
                len(signature(method).parameters),
                permission
            )
            def new(*args):
                method(*args)
            return new
        return decorator

command_manager = CommandManager()


class CommandException(Exception):
    """Empty exception"""
    pass
