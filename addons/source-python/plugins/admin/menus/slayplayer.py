from menus import PagedMenu, PagedOption, Text
from filters.players import PlayerIter

from ..strings import menus
# from ..mainmenu import MainMenu
from .playercommands import PlayerCommandsMenu


__all__ = (
    'SlayPlayer'
)

class SlayPlayer(PlayerCommandsMenu):
    """Menu used to kick players"""

    caption = 'Tuer un joueur'
    needed_flag = 'a'

    @staticmethod
    def select(menu, index, choice):
        """Kick player"""
        choice.value.slay()

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )
