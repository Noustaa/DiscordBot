from discord.ext import commands


class MultiplicationEgyptienne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="egy")
    async def run(self, ctx: commands.Context, numberA: int, numberB: int):
        a = numberA
        b = numberB
        # noinspection PyPep8Naming
        z = 0
        while a != 0:
            if a % 2 != 0:
                z = z + b
            b = b + b
            a = int(a / 2)
        await ctx.channel.send("Resultat = " + str(z))


def setup(bot):
    bot.add_cog(MultiplicationEgyptienne(bot))
