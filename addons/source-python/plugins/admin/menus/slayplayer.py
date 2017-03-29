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
        Punishment.slay(choice.value, owner=index)
        return menu

    @staticmethod
    def build(menu, index):
        """List players"""
        menu.clear()
        for player in PlayerIter():
            menu.append(PagedOption(player.name, player))

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )
