## IMPORTS

from filters.players import PlayerIter
from menus import ListMenu
from menus import ListOption
from menus import PagedMenu
from menus import PagedOption
from menus import Text
from paths import GAME_PATH
from messages import SayText2
from engines.server import engine_server
from listeners.tick import Delay

import .menus
from ..utils import get_map_list
from ..strings import menus, messages

## ALL DECLARATION

__all__ = (
    'changemap_menu',
)


#
#   CHANGE MAP
#
def _on_changemap_build(menu, index):
    menu.clear()
    for mapName in get_map_list():
        menu.append(PagedOption(mapName, mapName))


def _on_changemap_select(menu, index, choice):
    Delay(3, engine_server.change_level, (choice.value, None,))
    SayText2(messages['Change Map'].format(name=choice.value, duration=3)).send()


changemap_menu = PagedMenu(
    title=menus['Map Menu'],
    build_callback=_on_changemap_build,
    select_callback=_on_changemap_select,
    parent_menu=player_menu,
)
