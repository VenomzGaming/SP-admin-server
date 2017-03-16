from collections import defaultdict
from inspect import signature

## ALL DECLARATION

__all__ = (
    'command_manager',
)


class CommandManager(defaultdict):

    def __missing__(self, item):
        return (None, None)

    def add_command(self, command, flag):
        if command in self:
            raise CommandException('Cannot re-assign command ({command_name})'.format(
                command_name=command))
        def decorator(method):
            self[command] = (method,
                ## Retrieves the functions argument count. Used to verify the client/say command is valid.
                len(signature(method).parameters),
                flag
                )
            def new(*args):
                method(*args)
            return new
        return decorator

command_manager = CommandManager()


class CommandException(Exception):
    pass
