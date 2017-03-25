## IMPORTS

from collections import defaultdict
from engines.server import engine_server


## DECLARTIONS

__all__ = (
    'check_permission',
)


# def check_permission(player, character):
#     if character in admin_permissions[player.steamid]:
#         return True
#     else:
#         engine_server.client_printf(player.edict,
#             'CA - You do not have permissions to use this command.\n')
#         return False

def check_permission(player, permission):
    if permission in player.permissions:
        return True
    else:
        return False
