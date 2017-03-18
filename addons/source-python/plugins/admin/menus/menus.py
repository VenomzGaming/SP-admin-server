## IMPORTS

from menus import ListMenu
from menus import ListOption
from menus import PagedMenu
from menus import PagedOption
from menus import Text

from .punishments import slay_menu, kick_menu, ban_menu, mute_menu
from .servers import changemap_menu
from ..strings import menus

## ALL DECLARATION

__all__ = (
    'player_menu',
    'server_menu',
    'voting_menu',
    'main_menu',
)


#
#   PLAYER MENU
#
def _on_player_menu_select(menu, index, choice):
    if choice.value in _player_menu_selections:
        return _player_menu_selections[choice.value]


player_menu = PagedMenu(
    title=menus['Player Menu'],
    select_callback=_on_player_menu_select,
    data=[
        PagedOption(menus['Mute Menu'], 1),
        PagedOption(menus['Slay Menu'], 2),
        PagedOption(menus['Kick Menu'], 3),
        PagedOption(menus['Ban Menu'], 4)
    ]
)


_player_menu_selections = {
    1: mute_menu,
    2: slay_menu,
    3: kick_menu,
    4: ban_menu
}

#
#   SERVER MENU
#
def _on_server_menu_select(menu, index, choice):
    if choice.value in _server_menu_selections:
        return _server_menu_selections[choice.value]


server_menu = PagedMenu(
    title=menus['Server Menu'],
    select_callback=_on_server_menu_select,
    data=[
        PagedOption(menus['Change Map'], 1)
    ]
)


_server_menu_selections = {
    1: changemap_menu
}


#
#   VOTING MENU
#
def _on_voting_menu_select(menu, index, choice):
    if choice.value in _voting_menu_selections:
        return _voting_menu_selections[choice.value]


voting_menu = PagedMenu(
    title=menus['Voting Menu'],
    select_callback=_on_voting_menu_select,
    data=[
        PagedOption('Kicker un joueur', 1),
        PagedOption('Changer de map', 2)
    ]
)


_voting_menu_selections = {
    # 1: kick_player,
    # 2: changemap
}


#
#   MAIN
#
def _on_main_menu_select(menu, index, choice):
    if choice.value in _main_menu_selections:
        return _main_menu_selections[choice.value]


main_menu = PagedMenu(
    title=menus['Main Menu'],
    select_callback=_on_main_menu_select,
    data=[
        PagedOption(menus['Player Menu'], 1),
        PagedOption(menus['Server Menu'], 2),
        PagedOption(menus['Voting Menu'], 3)
    ]
)


_main_menu_selections = {
    1: player_menu,
    2: server_menu,
    3: voting_menu
}
