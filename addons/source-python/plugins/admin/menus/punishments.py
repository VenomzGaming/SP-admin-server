## IMPORTS

from filters.players import PlayerIter
from menus import ListMenu
from menus import ListOption
from menus import PagedMenu
from menus import PagedOption
from menus import Text
from paths import GAME_PATH
from messages import SayText2
from players.entity import Player
from engines.server import engine_server
from listeners.tick import Delay

from ..strings import menus, messages, reasons_messages

## ALL DECLARATION

__all__ = (
    'mute_menu',
    'slay_menu',
    'kick_menu',
    'ban_menu',
)


#
#  MUTE PLAYER
#
def _on_mute_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        muted = ' [MUTED]' if player.is_muted else ''
        menu.append(PagedOption(player.name + muted, player))


def _on_mute_player_select(menu, index, choice):
    # Not work
    if choice.value.is_muted:
        choice.value.unmute()
        SayText2(messages['Unmute']).send(index)
    else:
        choice.value.mute()
        SayText2(messages['Mute']).send(index)


mute_menu = PagedMenu(
    title=menus['Mute Menu'],
    build_callback=_on_mute_player_build,
    select_callback=_on_mute_player_select,
    # parent_menu=player_menu,
)

#
#  SLAY PLAYER
#
def _on_slay_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))


def _on_slay_player_select(menu, index, choice):
    choice.value.slay()
    SayText2(messages['Slay']).send(index)


slay_menu = PagedMenu(
    title=menus['Slay Menu'],
    build_callback=_on_slay_player_build,
    select_callback=_on_slay_player_select,
    # parent_menu=player_menu,
)


#
#  KICK PLAYER
#
def _on_kick_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))


def _on_kick_player_select(menu, index, choice):
    choice.value.kick()


kick_menu = PagedMenu(
    title=menus['Kick Menu'],
    build_callback=_on_kick_player_build,
    select_callback=_on_kick_player_select,
    # parent_menu=player_menu,
)


#
#   BAN PLAYER
#
def _on_ban_player_build(menu, index):
    menu.clear()
    for player in PlayerIter(not_filters='bot'):
        menu.append(PagedOption(player.name, player))


def _on_ban_player_select(menu, index, choice):
    ban_duration.player = choice.value
    return ban_duration


def _on_ban_duration_build(menu, index):
    menu.clear()
    menu.append(PagedOption(menus['1 Hour'], 60))
    menu.append(PagedOption(menus['2 Hour'], 120))
    menu.append(PagedOption(menus['4 Hour'], 240))
    menu.append(PagedOption(menus['1 Day'], 1440))
    menu.append(PagedOption(menus['2 Day'], 2880))
    menu.append(PagedOption(menus['7 Day'], 10080))
    # menu.append(PagedOption(menus['Permanent'], 0))


def _on_ban_duration_select(menu, index, choice):
    ban_reasons.player = menu.player
    ban_reasons.duration = choice.value
    return ban_reasons


def _on_ban_reason_build(menu, index):
    menu.clear()
    reasons_list = reasons_messages['reasons'][str(Player(index).language)[:2]]['ban']

    for reasons in reasons_list:
        menu.append(PagedOption(reasons, reasons))


def _on_ban_reason_select(menu, index, choice):
    ban_reasons.player.ban(duration=ban_reasons.duration, kick=False, write_ban=True)
    ban_reasons.player.kick(choice.value)


ban_menu = PagedMenu(
    title=menus['Ban Menu'],
    build_callback=_on_ban_player_build,
    select_callback=_on_ban_player_select,
    # parent_menu=player_menu,
)

ban_duration = PagedMenu(
    title=menus['Ban Menu'],
    build_callback=_on_ban_duration_build,
    select_callback=_on_ban_duration_select,
    parent_menu=ban_menu,
)

ban_reasons = PagedMenu(
    title=menus['Ban Menu'],
    build_callback=_on_ban_reason_build,
    select_callback=_on_ban_reason_select,
    parent_menu=ban_duration,
)
