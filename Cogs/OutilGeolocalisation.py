from discord.ext import commands


class OutilGeolocalisation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="syracuse")
    async def run(self, ctx: commands.Context):
        pass

    @run.error
    async def run_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Inccorrect arguments entered | **!command_name - outcome:str - amount:int')

def setup(bot):
    bot.add_cog(OutilGeolocalisation(bot))
