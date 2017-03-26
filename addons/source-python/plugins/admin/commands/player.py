## IMPORTS

import re
from commands.typed import TypedClientCommand, TypedSayCommand, TypedServerCommand, CommandReturn
from messages import SayText2
from players.entity import Player

from .filters import Filter
from .manager import command_manager
from ..permissions import on_permission_failed
from .punishment import Punishment
from ..strings import messages


## GLOBAL

# Admin string
ADMIN_STRING = messages['Admin']


## CLASS COMMAND PUNISHMENT

class CommandPunishment:

    def __init__(self, command_info):
        self.type, self.filter, self.args = self._parse_command(command_info)
        self.caller = Player(command_info.index) if command_info.index is not None else None
        self.target = self._get_player()

    @staticmethod
    def _parse_command(command_info):
        command = list(command_info.command)
        command_name = re.sub(r'(!|/|sp_)', '', command[0])
        command_filter = command[1]
        args = ','.join(command[2:])
        return (command_name, command_filter, args)


    def _get_player(self):
        find = None
        players = [user for user in Filter(self.filter, self.caller)]

        if len(players) == 0:
            if self.caller is not None:
                SayText2(messages['Not Found']).send(self.caller.index)
            else:
                print('Player not found.')
        else:
            find = players

        return find

    def punish_player(self):
        if not isinstance(self.target, list):
            getattr(Punishment, self.type)(self.target, self.args)
        else: 
            for target in self.target:
                getattr(Punishment, self.type)(target, self.args)


## ADMIN COMMANDS
    
@TypedSayCommand('!kick', 'admin.kick', on_permission_failed)
@TypedSayCommand('/kick', 'admin.kick', on_permission_failed)
@TypedServerCommand('sp_kick', 'admin.kick')
def _command_kick(command_info, filter_value:str):
    command = CommandPunishment(command_info)
    command.punish_player()
    return CommandReturn.BLOCK


@TypedSayCommand('!ban', 'admin.ban', on_permission_failed)
@TypedSayCommand('/ban', 'admin.ban', on_permission_failed)
@TypedServerCommand('sp_ban', 'admin.ban')
def _command_ban(command_info, filter_value:str, duration:int):
    command = CommandPunishment(command_info)
    command.punish_player()
    return CommandReturn.BLOCK


@TypedSayCommand('!slay', 'admin.slay', on_permission_failed)
@TypedSayCommand('/slay', 'admin.slay', on_permission_failed)
@TypedServerCommand('sp_slay', 'admin.slay')
def _command_slay(command_info, filter_value:str):
    command = CommandPunishment(command_info)
    command.punish_player()
    return CommandReturn.BLOCK


