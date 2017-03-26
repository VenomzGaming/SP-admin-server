## IMPORTS

from messages import SayText2
from players.entity import Player

from ..strings import messages

## DECLARATIONS

__all__ = (
    'Punishment'
)


class Punishment:
    """Commands about players"""

    @classmethod
    def kick(cls, player, *args):
        """Kick a player"""
        player.kick()

    @classmethod
    def ban(cls, player, *args):
        """Kick a player"""
        if len(args) == 0:
            player.ban(kick=True, write_ban=True)
        else:
            player.ban(duration=args[0], kick=True, write_ban=True)
 

    @classmethod
    def slay(cls, player, *args):
        """Slay a player"""
        if not player.dead:
            player.slay()
            SayText2(messages['Slay']).send(player.index)
        
