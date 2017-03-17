## IMPORTS

from filters.players import PlayerIter
from players.entity import Player

from fuzzywuzzy import process

## ALL DECLARATION

__all__ = (
    'Filter',
)


class Filter:

    def __init__(self, string_to_filter, caller):
        self._symbols = {
            '@': self._by_selector,
            '#': self._by_name,
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
        elif argument in ('me', 'self'):
            self._add_player(self._caller)


    def _by_name(self, argument):
        players = {player.name: player for player in PlayerIter()}
        ## Fuzzywuzzy is used to trace a name to a player.
        name, percent = process.extractOne(argument, players.keys())
        if percent <= 60:
            ## Return, because it is likely they have given a name too inaccurate.
            return
        self._add_player(players[name])

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
