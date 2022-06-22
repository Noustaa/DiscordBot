from discord.ext import commands


# class that defines the custom help command
class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    # method that is called when executing !help, it will list all available commands and their descriptions from cogs
    async def send_bot_help(self, mapping):
        for cog in mapping:
            await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in mapping[cog]]} - '
                                              f'{[command.description for command in mapping[cog]]}')

    # method that is called when executing !help <cog_name>, it will list all available commands in a specific cog
    # and their descriptions
    async def send_cog_help(self, cog):
        await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]} -'
                                          f' {[command.description for command in cog.get_commands()]}')

    # method that is called when executing !help <command_name>, it will display the specific command description
    async def send_command_help(self, command):
        await self.get_destination().send(f'{command.name} - {command.description}')
