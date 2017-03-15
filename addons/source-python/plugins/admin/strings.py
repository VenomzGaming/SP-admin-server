## IMPORTS

from translations.strings import LangStrings

from .info import info

## ALL DECLARATION

__all__ = (
	'menus',
)

## GLOBALS

menus = LangStrings(info.basename / 'menus')
