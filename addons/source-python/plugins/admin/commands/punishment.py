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
    def ban(cls, player, duration, **kwargs):
        """Ban a player"""
        if len(kwargs) == 0:
            player.ban(kick=True, write_ban=True)
        else:
            if 'reason' in kwargs:
                player.ban(duration=duration, kick=False, write_ban=True)
                player.kick(kwargs['reason'])
            else:
                player.ban(duration=duration, kick=True, write_ban=True)


    @classmethod
    def slay(cls, player, **kwargs):
        """Slay a player"""
        if not player.dead:
            player.slay()
            SayText2(messages['Slay']).send(player.index)
        else:
            SayText2(messages['Already Dead']).send(kwargs['owner'])


    @classmethod
    def mute(cls, player, *args):
        """Mute a player"""
        if player.is_muted():
            player.unmute()
            SayText2(messages['Unmute']).send(player.index)
        else:
            player.mute()
            SayText2(messages['Mute']).send(player.index)
        
        
