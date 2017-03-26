from menus import PagedMenu, PagedOption, Text
from filters.players import PlayerIter

from admin.commands.punishment import Punishment
from .playercommands import PlayerCommandsMenu
from ..strings import menus


__all__ = (
    'KickPlayer'
)

class KickPlayer(PlayerCommandsMenu):
    """Menu used to kick players"""

    caption = 'Kicker un joueur'
    needed_flag = 'admin.kick'

    @staticmethod
    def select(menu, index, choice):
        """Kick player"""
        Punishment.kick(choice.value)

    @staticmethod
    def build(menu, index):
        """List players"""
        menu.clear()
        for player in PlayerIter(not_filters='bot'):
            menu.append(PagedOption(player.name, player))

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )
