# SP-admin-server
Server part of our SourcePython admin panel by the Venomz Multigaming. You can visit our [website](https://venomz.fr), [forums](https://forum.venomz.fr), or come play with us on our [teamspeak3 server](ts3server://ts.venomz.fr/?port=9988)


# Installation
1. Clone the repository
2. Install it under the `addons/source-python/plugins` folder of your game server
3. Go edit the `permissions.py` file to setup your admins permissions. The `admin_config` object is a json object should look like
```
{
	'<steam_id_v3>': '<list of permissions>',
	'STEAM_1:0:26270590': 'a', # Example, will have the 'a' flag
	'STEAM_1:0:26270591': 'abe' # Example, will have the 'a', 'b' AND 'e' flag
}
```

# Development
You can add a new command with the decorator `@command_manager.add_command(<command_name>, <needed_flag>)`.
For example
```
@command_manager.add_command('sp_admin', 'a') # This command can be triggered by typping 'sp_admin' in the game console and the triggerer needs the 'a' flag.
def _show_admin_menu(player):
	main_menu.send(player)
```

# Contributions
Feel free to fork the repository and make some improvements, all contributions are welcome =)

# Particular thanks and attributions
This plugin is based on the [Client Admin by Predz](https://github.com/Predz/Client-Admin).
