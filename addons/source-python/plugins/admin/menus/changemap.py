from menus import PagedMenu, PagedOption, Text
from filters.players import PlayerIter
from messages import SayText2
from engines.server import engine_server
from listeners.tick import Delay

from ..strings import menus, messages
from .servercommands import ServerCommandsMenu
from ..utils.utils import get_map_list


__all__ = (
    'ChangeMap'
)

class ChangeMap(ServerCommandsMenu):
    """Menu used to change map"""

    caption = menus['Change Map']
    needed_flag = 'admin.map'

    @staticmethod
    def select(menu, index, choice):
        """Change map"""
        Delay(3, engine_server.change_level, (choice.value, None,))
        for player in PlayerIter('human'):
            SayText2(messages['Change Map'].get_string(
                player.language[:2],
                name=choice.value, 
                duration=3)
            ).send()

    @staticmethod
    def build(menu, index):
        """List maps"""
        menu.clear()
        for map_name in get_map_list():
            menu.append(PagedOption(map_name, map_name))

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )
