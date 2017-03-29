from menus import PagedMenu, PagedOption, Text
from filters.players import PlayerIter

from admin.commands.punishment import Punishment
from .playercommands import PlayerCommandsMenu
from ..strings import menus


__all__ = (
    'MutePlayer'
)

class MutePlayer(PlayerCommandsMenu):
    """Menu used to mute players"""

    caption = menus['Mute Menu']
    needed_flag = 'admin.mute'

    @staticmethod
    def select(menu, index, choice):
        """Mute player"""
        Punishment.mute(choice.value)
        return menu

    @staticmethod
    def build(menu, index):
        """List players"""
        menu.clear()
        for player in PlayerIter('human'):
            muted = menus['Muted'][player.language[:2]] if player.is_muted() else ''
            menu.append(PagedOption(menus['Mute Player'].get_string(
                player=player.name, 
                state=muted), 
            player))

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )
