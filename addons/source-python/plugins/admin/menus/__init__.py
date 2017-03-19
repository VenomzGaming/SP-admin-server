# from admin.menus.menus import MainMenu, player_menu, server_menu, VotingMenu
# from admin.menus.punishments import kick_menu, slay_menu, ban_menu

from os.path import dirname, basename, isfile
from glob import glob

# ## INIT ALL MENUS

modules = glob(dirname(__file__) + '/*.py')
menus = tuple(basename(f)[:-3] for f in modules if isfile(f))

__all__ = menus
