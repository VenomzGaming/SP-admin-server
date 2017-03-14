## IMPORTS

import collections
from collections import OrderedDict
from filters.players import PlayerIter
from players.helpers import userid_from_index
from menus import ListMenu
from menus import ListOption
from menus import PagedMenu
from menus import PagedOption
from menus import Text
from paths import GAME_PATH
from messages import SayText2
from engines.server import engine_server
from listeners.tick import Delay

import pprint

__all__ = (
    'main_menu',
    'kick_player',
    'changemap',
    )

#
#   Utils
#

def get_map_list():
    maplist = GAME_PATH / 'maplist.txt'
    if not maplist.isfile():
        raise FileNotFoundError("Missing {}".format('maplist'))

    rs = []
    with open(maplist) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith('//'):
                continue

            rs.append(line)
    return rs

def change_map(level):
    engine_server.change_level(level, None)

#
#   Kickplayer
#

def _on_kick_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))

def _on_kick_player_select(menu, index, choice):
	choice.value.kick();

#
#   Changemap
#

def _on_changemap_build(menu, index):
    menu.clear()
    for mapName in get_map_list():
    	menu.append(PagedOption(mapName, mapName))

def _on_changemap_select(menu, index, choice):
    Delay(3, change_map, (choice.value,))
    SayText2('Changing map for {} in 3 seconds'.format(choice.value)).send()

#
#   MAIN
#

def _on_main_menu_select(menu, index, choice):
    if choice.value in _main_menu_selections:
        return _main_menu_selections[choice.value]

main_menu = PagedMenu(
    title='Venomz admin menu',
    select_callback=_on_main_menu_select,
    data=[
        PagedOption('Kicker un joueur', 1),
        PagedOption('Changer de map', 2)
    ]
)

kick_player = PagedMenu(
    title='Kicker un joueur',
    build_callback=_on_kick_player_build,
    select_callback=_on_kick_player_select,
    parent_menu=main_menu,
)

changemap = PagedMenu(
    title='Changer de map',
    build_callback=_on_changemap_build,
    select_callback=_on_changemap_select,
    parent_menu=main_menu,
)

_main_menu_selections = {
    1: kick_player,
    2: changemap
}
