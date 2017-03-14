## IMPORTS

from config.manager import ConfigManager
from translations.strings import LangStrings

from .info import info

## ALL DECLARATION

__all__ = (
    'g_configs',
)

## GLOBALS

g_configs = dict()

with ConfigManager(info.name) as _config:

    #
    #   Vip Advantages
    #
    _config.section('Vip Advantages')

    g_configs['add_health'] = _config.cvar(
        'add_health', 5,
        'How many HP add to the player on spawn | Default : 5', 0)
