from discord.ext import commands


class MultiplicationEgyptienne(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # defines the actual command
    @commands.command(name="egy",
                      description="Cette commande execute la multiplication egyptienne de deux entier. "
                                  "Utilisation: !egy nombreA nombreB")
    async def run(self, ctx: commands.Context, numberA: int, numberB: int):
        a = numberA
        b = numberB
        z = 0
        while a != 0:
            if a % 2 != 0:
                z = z + b
            b = b + b
            # casting int to keep only the integer part from the division (rule from egyptian multiplication method)
            a = int(a / 2)

        # sends the result back to the discord channel
        await ctx.channel.send("Resultat = " + str(z))

    # error triggered on incorrect command formatting
    @run.error
    async def run_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Incorrect arguments entered | Usage : !egy number1 numberB')


# adds the commands to the bot
def setup(bot):
    bot.add_cog(MultiplicationEgyptienne(bot))
