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
	pass
