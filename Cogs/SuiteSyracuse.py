from discord.ext import commands


class SuiteSyracuse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="syr")
    async def run(self, ctx: commands.Context, number: int):
        # noinspection PyPep8Naming
        listToDisplay = [number]
        while listToDisplay[-1] != 1:
            if listToDisplay[-1] % 2 == 0:
                listToDisplay.append(int(listToDisplay[-1]/2))
            else:
                listToDisplay.append(int(listToDisplay[-1]*3+1))
        await ctx.channel.send(listToDisplay)

    @run.error
    async def run_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Incorrect arguments entered | **!command_name - outcome:str - amount:int')


def setup(bot):
    bot.add_cog(SuiteSyracuse(bot))
