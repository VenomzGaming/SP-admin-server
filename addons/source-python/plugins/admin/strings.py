## IMPORTS

from translations.strings import LangStrings

from .info import info

## ALL DECLARATION

__all__ = (
	'strings',
)

## GLOBALS

strings = LangStrings(info.basename + '/' + 'strings')
