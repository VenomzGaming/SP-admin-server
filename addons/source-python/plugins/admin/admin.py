## IMPORTS

import menus
from .commands.manager import command_manager
from .commands.filters import Filter
from .permissions import check_permission

import admin.menus
from admin.menus.menus import main_menu

## LOAD / UNLOAD

def load():
    pass


def unload():
    pass


@command_manager.add_command('sp_admin', 'a')
def _show_admin_menu(player):
    main_menu.send(player)
