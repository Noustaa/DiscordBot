from discord.ext import commands
import os


class NoussBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")
        # Load all commands
        for file in os.listdir("./Cogs"):  # lists all the cog files inside the cog folder.
            if file.endswith(".py"):  # It gets all the cogs that ends with a ".py".
                self.load_extension(f"Cogs.{file.removesuffix('.py')}")  # This loads the cog.

    # noinspection PyMethodMayBeStatic
    async def on_ready(self):
        print("Le bot est prêt.")

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send("No such command")
