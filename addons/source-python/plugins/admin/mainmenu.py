from menus import SimpleMenu, SimpleOption, Text
from messages import SayText2

from .strings import menus
from .permissions import check_permission
from players.entity import Player

from pprint import pprint

class AdminMenu:
    """Main admin menu, entrypoint for admins"""

    caption = 'Menu principal'

    @classmethod
    def _build_submenus(cls, menu, index):
        """Auto build menus which inherit from the current menu"""
        i = 1
        for subcls in cls.__subclasses__():
            try:
                if check_permission(Player(index), subcls.needed_flag):
                    menu.append(SimpleOption(i, subcls.caption, subcls.menu()))
            except AttributeError:
                menu.append(SimpleOption(i, subcls.caption, subcls.menu()))
            i += 1

    @staticmethod
    def select(menu, index, choice):
        """Auto switch menus on selection and set parent menu to current"""
        next_menu = choice.value
        if next_menu is not None:
            next_menu.parent_menu = menu
            return next_menu

    @classmethod
    def build(cls, menu, index):
        """Auto build a SimpleMenu with his caption, back link if needed and close button"""
        menu.clear()
        menu.append(Text(cls.caption))
        cls._build_submenus(menu, index)
        if cls.__name__ != 'AdminMenu':
            try:
                menu.append(SimpleOption(7, menus['Back'], menu.parent_menu, highlight=False))
            except AttributeError:
                pass
        menu.append(SimpleOption(9, menus['Close'], highlight=False))

    @classmethod
    def menu(cls):
        """Returns the menu object"""
        return SimpleMenu(
            build_callback=cls.build,
            select_callback=cls.select
        )
