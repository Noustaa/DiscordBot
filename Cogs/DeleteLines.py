from discord.ext import commands


class DeleteLines(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="del")
    async def run(self, ctx: commands.Context, number: int = 5):
        messages = await ctx.channel.history(limit=number + 1).flatten()

        for each_message in messages:
            await each_message.delete()


def setup(bot):
    bot.add_cog(DeleteLines(bot))
