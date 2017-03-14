## IMPORTS

from menus import ListMenu
from menus import ListOption
from menus import PagedMenu
from menus import PagedOption
from menus import Text

from .punishments import *
from .servers import *
from .voting import *

## ALL DECLARATION

__all__ = (
    'main_menu',
    'player_menu',
    'server_menu',
    'voting_menu',
)


#
#   MAIN
#
def _on_main_menu_select(menu, index, choice):
    if choice.value in _main_menu_selections:
        return _main_menu_selections[choice.value]

_main_menu_selections = {
    1: player_menu,
    2: changemap
}

main_menu = PagedMenu(
    title='Venomz admin menu',
    select_callback=_on_main_menu_select,
    data=[
        PagedOption('Kicker un joueur', 1),
        PagedOption('Changer de map', 2)
    ]
)


#
#   PLAYER MENU
#
def _on_player_menu_select(menu, index, choice):
    if choice.value in _player_menu_selections:
        return _player_menu_selections[choice.value]

_player_menu_selections = {
    1: kick_player,
    2: changemap
}

player_menu = PagedMenu(
    title='Manage Player',
    select_callback=_on_player_menu_select,
    data=[
        PagedOption('Kicker un joueur', 1),
        PagedOption('Changer de map', 2)
    ]
)


#
#   SERVER MENU
#
def _on_server_menu_select(menu, index, choice):
    if choice.value in _server_menu_selections:
        return _server_menu_selections[choice.value]

_server_menu_selections = {
    1: kick_player,
    2: changemap
}

server_menu = PagedMenu(
    title='Server Management',
    select_callback=_on_server_menu_select,
    data=[
        PagedOption('Kicker un joueur', 1),
        PagedOption('Changer de map', 2)
    ]
)


#
#   VOTING MENU
#
def _on_voting_menu_select(menu, index, choice):
    if choice.value in _voting_menu_selections:
        return _voting_menu_selections[choice.value]

_voting_menu_selections = {
    1: kick_player,
    2: changemap
}

voting_menu = PagedMenu(
    title='Manage Player',
    select_callback=_on_voting_menu_select,
    data=[
        PagedOption('Kicker un joueur', 1),
        PagedOption('Changer de map', 2)
    ]
)
