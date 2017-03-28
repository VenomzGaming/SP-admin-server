from menus import PagedMenu, PagedOption, Text
from filters.players import PlayerIter


from admin.commands.punishment import Punishment
from ..strings import menus
from .playercommands import PlayerCommandsMenu


__all__ = (
    'SlayPlayer'
)

class SlayPlayer(PlayerCommandsMenu):
    """Menu used to kick players"""

    caption = menus['Slay Menu']
    needed_flag = 'admin.slay'

    @staticmethod
    def select(menu, index, choice):
        """Slay player"""
        Punishment.slay(choice.value)

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )
