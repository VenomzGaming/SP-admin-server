import collections
from collections import OrderedDict
from filters.players import PlayerIter
from players.helpers import userid_from_index
from menus import Text
from paths import GAME_PATH


__all__ = (
    'get_map_list',
)


##   UTILS


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
