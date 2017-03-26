## IMPORTS

from fuzzywuzzy import process

from filters.players import PlayerIter
from players.entity import Player


## ALL DECLARATION

__all__ = (
    'Filter',
)


class Filter:
    """This class provides some basic filters to iterate through players"""

    def __init__(self, string_to_filter, caller):
        self._symbols = {
            '@': self._by_selector,
            '#': self._by_userid,
            '%': self._by_name,
        }

        self._caller = caller
        self._string = string_to_filter
        self._parts = string_to_filter.split(',')
        self._group = list()

        for _part in self._parts:
            symbol, arg = self._break_symbol_from_argument(_part)

            filter_func = self._get_symbol_filter(symbol)
            filter_func(arg)

    def __iter__(self):
        for player in self._group:
            yield player

    def _by_selector(self, argument):
        if argument in PlayerIter._filters:
            for target in PlayerIter(argument):
                self._add_player(target)
        elif self._caller is not None and argument in ('me', 'self'):
            self._add_player(self._caller)


    def _by_name(self, argument):
        """Returns a list of players by their name"""
        players = {player.name: player for player in PlayerIter()}
        ## Fuzzywuzzy is used to trace a name to a player.
        name, percent = process.extractOne(argument, players.keys())
        if percent <= 60:
            return
        self._add_player(players[name])


    def _by_userid(self, argument):
        """Returns the player with this userid"""
        try:
            player = Player.from_userid(int(argument))
        except ValueError:
            return

        self._add_player(player)


    def _exists_by_attribute(self, value, attribute):
        for player in self._group:
            if getattr(player, attribute) == value:
                return True
        return False


    def _add_player(self, target):
        if self._exists_by_attribute(target.userid, 'userid'):
            return
        self._group.append(target)


    def _break_symbol_from_argument(self, part):
        """Used to split symbol from arguments"""
        symbol = part[0]
        argument = part[1:]
        if not symbol in self._symbols:
            raise ValueError(
                'Command ({}) contains identifier ({}) with no usable symbol.'.format(
                    self._string, part)
                )
        return symbol, argument

    def _get_symbol_filter(self, symbol):
        return self._symbols[symbol]
