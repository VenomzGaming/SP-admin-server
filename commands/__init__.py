'''

	Command management for admin systems.
	... Decorators allow for easy input into
	the menus.

'''

from .filters import Filter
from .manager import command_manager
from ..permissions import check_permission

## ========== FILTER ALL CLIENT COMMANDS ============

''' Filtering all client and say commands. '''

from commands import CommandReturn
from commands.client import ClientCommandFilter
from engines.server import engine_server
from players.entity import Player

@ClientCommandFilter
def on_client_command(array, index):
	command = array[0]

	if command in command_manager:
		try:
			method, length, flag = command_manager[command]
		except:
			method, length = command_manager[command]

		player = Player(index)

		if method and flag and check_permission(player, flag):
			args = [player]
			for i in range(1, len(array)):
				args.append(array[i])

			if len(args) == length:
				method(*args)

			else:
				engine_server.client_printf(player.edict,
					'CA - This command requires {} arguments.\n'.format(length))

			return CommandReturn.BLOCK

	return CommandReturn.CONTINUE



