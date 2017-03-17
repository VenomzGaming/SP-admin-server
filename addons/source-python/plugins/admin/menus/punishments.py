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
from ..strings import menus, messages

## ALL DECLARATION

__all__ = (
    'slay_menu',
    'kick_menu',
    'ban_menu',
)


#
#  SLAY PLAYER
#
def _on_slay_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))


def _on_slay_player_select(menu, index, choice):
    choice.value.slay();
    SayText2(messages['Slay']).send(index)


slay_menu = PagedMenu(
    title=menus['Slay Menu'],
    build_callback=_on_slay_player_build,
    select_callback=_on_slay_player_select,
    parent_menu=menus.player_menu,
)


#
#  KICK PLAYER
#
def _on_kick_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))


def _on_kick_player_select(menu, index, choice):
    choice.value.kick();


kick_menu = PagedMenu(
    title=menus['Kick Menu'],
    build_callback=_on_kick_player_build,
    select_callback=_on_kick_player_select,
    parent_menu=player_menu,
)


#
#   BAN PLAYER
#
def _on_ban_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))


def _on_ban_player_select(menu, index, choice):
    choice.value.ban();
    choice.value.kick('Reason');


ban_menu = PagedMenu(
    title=menus['Ban Menu'],
    build_callback=_on_kick_player_build,
    select_callback=_on_kick_player_select,
    parent_menu=player_menu,
)
