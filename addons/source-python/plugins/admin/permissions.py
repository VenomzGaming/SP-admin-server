## IMPORTS

from engines.server import engine_server
from messages import SayText2

from .strings import messages

## DECLARTIONS

__all__ = (
    'on_permission_failed',
    'check_permission',
)


##   PERMISSION

def on_permission_failed(player, args):
    SayText2(messages['No Perm']).send(player.index)


def check_permission(player, permission):
    if permission in player.permissions:
        return True
    else:
        on_permission_failed(player)
        return False
