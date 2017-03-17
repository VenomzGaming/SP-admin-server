## IMPORTS

import json

from paths import PLUGIN_DATA_PATH
from translations.strings import LangStrings

from .info import info

## ALL DECLARATION

__all__ = (
    # 'messages',
    'menus',
    'reasons',
)

## GLOBALS

messages = LangStrings(info.basename + '/' + 'messages')
menus = LangStrings(info.basename + '/' + 'menus')

## REASONS FILE

path = PLUGIN_DATA_PATH / info.basename / 'reasons.json'
with open(path, 'r') as f:
    reasons = json.load(f)
