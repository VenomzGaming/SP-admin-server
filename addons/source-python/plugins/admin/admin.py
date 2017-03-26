## IMPORTS

from events import Event
from messages import SayText2
from players.entity import Player

import menus
from .commands.manager import command_manager
from .commands.filters import Filter
from .commands import say, player
from .permissions import check_permission

from .menus import *
from .mainmenu import AdminMenu

## LOAD / UNLOAD

def load():
    pass


def unload():
    pass

@command_manager.add_command('sp_admin', 'admin.menu')
def _show_admin_menu(player):
    AdminMenu.menu().send(player)
