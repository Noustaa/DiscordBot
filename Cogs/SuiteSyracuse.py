from discord.ext import commands


class SuiteSyracuse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # defines the actual command
    @commands.command(name="syr",
                      description="Cette commande execute la suite de syracuse d'un entier. Utilisation: !syr nombre")
    async def run(self, ctx: commands.Context, number: int):
        listToDisplay = [number]
        while listToDisplay[-1] != 1:
            if listToDisplay[-1] % 2 == 0:
                listToDisplay.append(int(listToDisplay[-1]/2))
            else:
                listToDisplay.append(int(listToDisplay[-1]*3+1))

        # sends the result back to the discord channel
        await ctx.channel.send(listToDisplay)

    # error triggered on incorrect command formatting
    @run.error
    async def run_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Incorrect arguments entered | Usage : !syr number')


# adds the commands to the bot
def setup(bot):
    bot.add_cog(SuiteSyracuse(bot))
