from menus import SimpleMenu, SimpleOption, Text

from ..strings import menus
# from ..mainmenu import MainMenu
from ..mainmenu import AdminMenu

__all__ = (
    'ServerCommandsMenu'
)

class ServerCommandsMenu(AdminMenu):
    """Commands about players"""

    caption = 'Gestion du serveur'
    needed_flag = 'a'

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return SimpleMenu(
            build_callback=cls.build,
            select_callback=cls.select
        )
