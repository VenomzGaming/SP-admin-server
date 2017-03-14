from .commands.manager import command_manager
from .commands.filters import Filter
from .permissions import check_permission
from .menus import *

@command_manager.add_command('sp_admin', 'a')
def _show_admin_menu(player):
	main_menu.send(player)
