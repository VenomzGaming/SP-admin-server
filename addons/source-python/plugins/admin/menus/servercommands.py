from menus import SimpleMenu, SimpleOption, Text

from ..strings import menus
from ..mainmenu import AdminMenu

__all__ = (
    'ServerCommandsMenu'
)

class ServerCommandsMenu(AdminMenu):
    """Commands about server"""

    caption = menus['Server Menu']
    needed_flag = 'admin.server'

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return SimpleMenu(
            build_callback=cls.build,
            select_callback=cls.select
        )
