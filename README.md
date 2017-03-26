# SP-admin-server
Server part of our SourcePython admin panel by the Venomz Multigaming. You can visit our [Website](https://venomz.fr), [Forums](https://forum.venomz.fr), or come play with us on our Teamspeak3 server: ts.venomz.fr:9988

# Caution
This plugin is an alpha version, *we are still developping it* ! We reserve right to make non compatible editions to the plugin.

# Installation
1. Clone the repository
2. Upload it in the root of your game server
3. Use now Source-python auth system to give admin permission :
Let's add your admin in /cfg/source-python/auth/player.json
```
{
    "STEAM_1:0:18526267": {
        "permissions": [
            "admin.menu",
            "admin.player",
            "admin.kick"
        ]
    }
}
```

# Development
You can add a new command with the decorator `@command_manager.add_command(<command_name>, <permission>)`.
For example
```
# This command can be triggered by typping 'sp_admin' in the game console and 
the triggerer needs the 'admin.menu' permission.
@command_manager.add_command('sp_admin', 'admin.menu') 
def _show_admin_menu(player):
    AdminMenu.menu().send(player)
```

# Commands

<b>Admin chat commands :</b>
```
@ <msg:str> # Say in chat
@@ <msg:str> # Say in hint center
@@@ <msg:str> # Say in center of players screen
@@@@ <filter:str> <msg:str> # Send private message to target

!slay <filter:str>
!kick <filter:str>
!ban <filter:str> <duration:int>
```

<b>Filtering system :</b><br>
- <b>@</b> with sourcpeython filters (@all, @bot, @ct, @t ...) and two more @me and @self (Multiple targets returned)<br>
- <b>\#</b> used for filtering by userid (One target returned)<br>
- <b>%</b> used for filtering by username (One target returned)<br>

<b>Server command :</b><br>
You can also type in console sp_slay, sp_kick and sp_ban with same parametters of chat command.

# Contributions
Feel free to fork the repository and make some improvements, all contributions are welcome =)

# Particular thanks and attributions
This plugin is based on the [Client Admin by Predz](https://github.com/Predz/Client-Admin).
