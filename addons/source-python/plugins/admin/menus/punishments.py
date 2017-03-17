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

from .menus import player_menu

## ALL DECLARATION

__all__ = (
    'changemap_menu',
    'slay_menu',
    'kick_menu',
    'ban_menu',
)


#
#  SLAY PLAYER
#
slay_menu = PagedMenu(
    title='Slay un joueur',
    build_callback=_on_slay_player_build,
    select_callback=_on_slay_player_select,
    parent_menu=player_menu,
)

def _on_slay_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))

def _on_slay_player_select(menu, index, choice):
    choice.value.slay();
    SayText2('Slayed').send(index)


#
#  KICK PLAYER
#
kick_menu = PagedMenu(
    title='Kicker un joueur',
    build_callback=_on_kick_player_build,
    select_callback=_on_kick_player_select,
    parent_menu=main_menu,
)

def _on_kick_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))

def _on_kick_player_select(menu, index, choice):
	choice.value.kick();

#
#   BAN PLAYER
#
ban_menu = PagedMenu(
    title='Kicker un joueur',
    build_callback=_on_kick_player_build,
    select_callback=_on_kick_player_select,
    parent_menu=main_menu,
)

def _on_ban_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))

def _on_ban_player_select(menu, index, choice):
    choice.value.ban();
    choice.value.kick('Reason');

#
#   CHANGE MAP
#
changemap_menu = PagedMenu(
    title='Changer de map',
    build_callback=_on_changemap_build,
    select_callback=_on_changemap_select,
    parent_menu=main_menu,
)

def _on_changemap_build(menu, index):
    menu.clear()
    for mapName in get_map_list():
    	menu.append(PagedOption(mapName, mapName))

def _on_changemap_select(menu, index, choice):
    Delay(3, engine_server.change_level, (choice.value, None,))
    SayText2('Changing map for {} in 3 seconds'.format(choice.value)).send()
