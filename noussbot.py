import discord.ext.commands
from discord.ext import commands
import os
import logging
import CustomHelpCommand


class NoussBot(commands.Bot):
    # default constructor
    def __init__(self):
        # sets the command prefix and define the help command to a custom one
        super().__init__(command_prefix="!", help_command=CustomHelpCommand.CustomHelpCommand())

        # Load all bot commands with Cogs
        # lists all the cog files inside the cog folder.
        for file in os.listdir("./Cogs"):
            # It gets all the cogs that ends with a ".py".
            if file.endswith(".py"):
                # This loads the cog.
                self.load_extension(f"Cogs.{file.removesuffix('.py')}")

    # method that runs when the bot enters a ready state
    async def on_ready(self):
        print("Le bot est prêt.")
        logging.info("NoussBot is ready!")

    # method that runs everytime a message is sent on the discord channel
    async def on_message(self, message):
        # to ignore all the messages sent by the bot itself and the messages that doesn't start with command prefix "!"
        if message.author == self.user or not message.content.startswith("!"):
            return
        # process the bot command and wait it to finish
        await self.process_commands(message)
        # logs the command into log file
        logging.info(str(message.author) + " used the command \"" + str(message.content) + "\"")

    # method that runs when there is a command error
    async def on_command_error(self, ctx: discord.ext.commands.Context, error):
        # check that the error type is commandNotFound
        if isinstance(error, commands.CommandNotFound):
            # the bot send a message on the discord channel to alert the user
            await ctx.channel.send("No such command")
            # logs it into log file
            logging.info(str(ctx.author) + " tried to use a not existing command \"" + str(ctx.message.content) + "\"")
