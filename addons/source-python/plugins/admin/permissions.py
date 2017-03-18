## IMPORTS

from collections import defaultdict
from engines.server import engine_server

admin_config = {
    'STEAM_1:0:26270590': 'a', # BlackWolf
    'STEAM_1:0:18526267': 'a' # Existenz
}


admin_permissions = defaultdict(str)
admin_permissions.update(admin_config)

## DECLARTIONS

__all__ = (
    'check_permission',
)


def check_permission(player, character):
    if character in admin_permissions[player.steamid]:
        return True
    else:
        engine_server.client_printf(player.edict,
            'CA - You do not have permissions to use this command.\n')
        return False
