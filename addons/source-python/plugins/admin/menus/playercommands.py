from menus import SimpleMenu, SimpleOption, Text

from ..strings import menus
# from ..mainmenu import MainMenu
from ..mainmenu import AdminMenu


__all__ = (
    'PlayerCommandsMenu'
)

class PlayerCommandsMenu(AdminMenu):
    """Commands about players"""

    caption = 'Gestion des joueurs'
    needed_flag = 'a'

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return SimpleMenu(
            build_callback=cls.build,
            select_callback=cls.select
        )
