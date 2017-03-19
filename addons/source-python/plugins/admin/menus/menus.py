## IMPORTS

from menus import ListMenu
from menus import ListOption
from menus import PagedMenu
from menus import PagedOption
from menus import Text
from menus import SimpleMenu
from menus import SimpleOption
from messages import SayText2

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

def _generic_simple_menu_select(menu, index, choice):
    next_menu = choice.value
    if next_menu is not None:
        next_menu.parent_menu = menu
        return next_menu

#
#   PLAYER MENU
#

def _player_menu_build(menu, index):
    menu.clear()
    menu.append(Text(menus['Player Menu']))
    menu.append(SimpleOption(1, menus['Mute Menu'], mute_menu))
    menu.append(SimpleOption(2, menus['Slay Menu'], slay_menu))
    menu.append(SimpleOption(3, menus['Kick Menu'], kick_menu))
    menu.append(SimpleOption(4, menus['Ban Menu'], ban_menu))
    menu.append(SimpleOption(7, menus['Back'], main_menu, highlight=False))
    menu.append(SimpleOption(9, menus['Close'], highlight=False))

player_menu = SimpleMenu(
    build_callback=_player_menu_build,
    select_callback=_generic_simple_menu_select
)

#
#   SERVER MENU
#

def _server_menu_build(menu, index):
    menu.clear()
    menu.append(Text(menus['Server Menu']))
    menu.append(SimpleOption(1, menus['Change Map'], changemap_menu))
    menu.append(SimpleOption(7, menus['Back'], main_menu, highlight=False))
    menu.append(SimpleOption(9, menus['Close'], highlight=False))

server_menu = SimpleMenu(
    build_callback=_server_menu_build,
    select_callback=_generic_simple_menu_select
)

#
#   VOTING MENU
#

def _voting_menu_build(menu, index):
    menu.clear()
    menu.append(Text(menus['Voting Menu']))
    menu.append(SimpleOption(1, menus['Kick Menu'], kick_menu))
    menu.append(SimpleOption(2, menus['Change Map'], changemap_menu))
    menu.append(SimpleOption(7, menus['Back'], main_menu, highlight=False))
    menu.append(SimpleOption(9, menus['Close'], highlight=False))

voting_menu = SimpleMenu(
    build_callback=_voting_menu_build,
    select_callback=_generic_simple_menu_select,
)

#
#   MAIN
#

main_menu = SimpleMenu(
    [
        Text(menus['Main Menu']),
        SimpleOption(1, menus['Player Menu'], player_menu),
        SimpleOption(2, menus['Server Menu'], server_menu),
        SimpleOption(3, menus['Voting Menu'], voting_menu),
        SimpleOption(9, menus['Close'], highlight=False)
    ],
    select_callback=_generic_simple_menu_select
)
