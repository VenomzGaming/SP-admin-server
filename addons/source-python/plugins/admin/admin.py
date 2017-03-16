## IMPORTS

import menus
from .commands.manager import command_manager
from .commands.filters import Filter
from .permissions import check_permission


## LOAD / UNLOAD

def load():
    pass


def unload():
    pass


@command_manager.add_command('sm_admin', 'a')
def _show_admin_menu(player):
    main_menu.send(player)
