## IMPORTS

from commands.typed import TypedClientCommand, TypedSayCommand, CommandReturn
from messages import SayText2, HintText, HudMsg
from players.entity import Player

from .filters import Filter
from .manager import command_manager
from ..permissions import on_permission_failed
from ..strings import messages


## GLOBALS

# Admin flag
ADMIN_CHAT_FLAG = "admin.chat"

# Admin string
ADMIN_STRING = messages['Admin']


## CHAT COMMAND

def add_name_prefix(player_index):
    return messages['Admin Prefix Message'].get_string(
        Player(player_index).language[:2],
        tag=ADMIN_STRING[Player(player_index).language[:2]], 
        name=Player(player_index).name
        )


def private_message(player, admin, msg):
    if admin is None:
        return

    SayText2(messages['Admin Whisp'].get_string(
            player.language[:2],
            recipient_name=player.name,
            admin=admin.name,
            msg=msg
        )).send(player.index)

    SayText2(messages['Admin Whisp'].get_string(
            admin.language[:2],
            recipient_name=player.name,
            admin=admin.name,
            msg=msg
        )).send(admin.index)


@TypedSayCommand('@', ADMIN_CHAT_FLAG, on_permission_failed)
def _command_admin_chat(command_info, *msg:str):
    if len(msg) == 0:
        return CommandReturn.BLOCK

    prefix = add_name_prefix(command_info.index)
    SayText2(messages['Admin Chat'].get_string(
        Player(command_info.index).language[:2],
        prefix=prefix,
        msg=' '.join(msg)
    )).send()

    return CommandReturn.BLOCK


@TypedSayCommand('@@', ADMIN_CHAT_FLAG, on_permission_failed)
def _command_hsay(command_info, *msg:str):
    if len(msg) == 0:
        return CommandReturn.BLOCK

    prefix = add_name_prefix(command_info.index)
    HintText(messages['Admin Message'].get_string(
        Player(command_info.index).language[:2],
        prefix=prefix,
        msg=' '.join(msg)
    )).send()

    return CommandReturn.BLOCK


@TypedSayCommand('@@@', ADMIN_CHAT_FLAG, on_permission_failed)
def _command_csay(command_info, *msg:str):
    if len(msg) == 0:
        return CommandReturn.BLOCK

    prefix = add_name_prefix(command_info.index)
    HudMsg(
        message=messages['Admin Message'].get_string(
            Player(command_info.index).language[:2],
            prefix=prefix, 
            msg=' '.join(msg)
            ),
        x=-1,
        y=-0.7,
    ).send()
    return CommandReturn.BLOCK


@TypedSayCommand('@@@@', permission=ADMIN_CHAT_FLAG)
def _command_psay(command_info, recipient, *msg:str):
    admin = Player(command_info.index)
    msg = ' '.join(msg)

    if len(msg) == 0:
        return CommandReturn.BLOCK

    if recipient[0:1] is '@':
        players = [user for user in Filter(recipient, admin) if user.userid != admin.userid]

        if len(players) == 0:
            SayText2(messages['Not Found']).send(admin.index)
            return CommandReturn.BLOCK

        i = 0
        for target in players:
            if i == 0:
                private_message(target, admin, msg)
            else:
                private_message(target, None, msg)
            i += 1
    else:
        player = [user for user in Filter(recipient, admin) if user.userid != admin.userid]

        if len(player) == 1:
            private_message(player[0], admin, msg)
        elif len(player) == 0:
            SayText2(messages['Not Found']).send(admin.index)
        else:
            SayText2(messages['More Than One']).send(admin.index)

    return CommandReturn.BLOCK

