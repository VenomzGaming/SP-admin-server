'''

	Permission management for access to
	commands and menus. Based upon using
	players steamids and ASCII characters.

'''

admin_config = {
	'STEAM_1:0:26270590': 'a' # BlackWolf
}

## ================ DEFAULT DICT ====================

from collections import defaultdict

admin_permissions = defaultdict(str)

admin_permissions.update(admin_config)

## =============== ALL DECLARTION ===================

__all__ = (
	'check_permission',
	)

## ================== DECORATOR =====================

from engines.server import engine_server

def check_permission(player, character):
	if character in admin_permissions[player.steamid]:
		return True
	else:
		engine_server.client_printf(player.edict,
			'CA - You do not have permissions to use this command.\n')
		return False
