from menus import PagedMenu, PagedOption, Text
from filters.players import PlayerIter
from players.entity import Player

from admin.commands.punishment import Punishment
from ..strings import menus
from .playercommands import PlayerCommandsMenu
from ..strings import menus, messages, reasons_messages


__all__ = (
    'BanPlayer'
)

class BanPlayer(PlayerCommandsMenu):
    """Menu used to ban players"""

    caption = menus['Ban Menu']
    needed_flag = 'admin.ban'

    @staticmethod
    def build(menu, index):
        """List players"""
        menu.clear()
        for player in PlayerIter('human'):
            menu.append(PagedOption(player.name, player))

    @staticmethod
    def select(menu, index, choice):
        """Show durations menu"""
        _menu = BanPlayerDuration.menu()
        _menu.player = choice.value
        return _menu

    @classmethod
    def menu(cls):
        """Return the menu object"""
        return PagedMenu(
            title=cls.caption,
            build_callback=cls.build,
            select_callback=cls.select
        )

class BanPlayerDuration:
    @classmethod
    def build(cls, menu, index):
        """Add all durations to the menu"""
        menu.clear()
        menu.append(PagedOption(menus['Hour'].get_string(Player(index).language[:2], hours=1), 60))
        menu.append(PagedOption(menus['Hours'].get_string(Player(index).language[:2], hours=2), 120))
        menu.append(PagedOption(menus['Hours'].get_string(Player(index).language[:2], hours=4), 240))
        menu.append(PagedOption(menus['Day'].get_string(Player(index).language[:2], days=1), 1440))
        menu.append(PagedOption(menus['Days'].get_string(Player(index).language[:2], days=2), 2880))
        menu.append(PagedOption(menus['Days'].get_string(Player(index).language[:2], days=7), 10080))

    @staticmethod
    def select(menu, index, choice):
        """Shows reasons menu"""
        _menu = BanPlayerReason.menu()
        _menu.player = menu.player
        _menu.duration = choice.value
        return _menu

    @classmethod
    def menu(cls):
        """Returns a menu with durations"""
        return PagedMenu(
            title=menus['Ban Duration'],
            build_callback=cls.build,
            select_callback=cls.select
        )

class BanPlayerReason:
    @classmethod
    def build(cls, menu, index):
        """Add reasons from reasons file into the menu"""
        menu.clear()
        reasons_list = reasons_messages['reasons'][Player(index).language[:2]]['ban']

        for reasons in reasons_list:
            menu.append(PagedOption(reasons, reasons))

    @staticmethod
    def select(menu, index, choice):
        """Proceed ban the player"""
        Punishment.ban(menu.player, menu.duration, reason=choice.value)
        # menu.player.ban(duration=menu.duration, kick=False, write_ban=True)
        # menu.player.kick(choice.value)
        return menu

    @classmethod
    def menu(cls):
        return PagedMenu(
            title=menus['Ban Reasons'],
            build_callback=cls.build,
            select_callback=cls.select
        )
