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
    def ban(cls, player, duration, *args):
        """Ban a player"""
        if len(args) == 0:
            player.ban(kick=True, write_ban=True)
        else:
            if len(args[0]) > 1:
                player.ban(duration=duration, kick=False, write_ban=True)
                player.kick(args[0])
            else:
                player.ban(duration=duration, kick=True, write_ban=True)


    @classmethod
    def slay(cls, player, *args):
        """Slay a player"""
        if not player.dead:
            player.slay()
            SayText2(messages['Slay']).send(player.index)


    @classmethod
    def mute(cls, player, *args):
        """Mute a player"""
        if player.is_muted():
            player.unmute()
            SayText2(messages['Unmute']).send(player.index)
        else:
            player.mute()
            SayText2(messages['Mute']).send(player.index)
        
        
