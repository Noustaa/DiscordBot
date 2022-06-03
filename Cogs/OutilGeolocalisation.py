from discord.ext import commands
from dotenv import load_dotenv
import shodan
import os
import re


class OutilGeolocalisation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        load_dotenv(dotenv_path="config")

    @commands.command(name="ip")
    async def run(self, ctx: commands.Context, hostname):
        ipv4_validator = re.compile(r"^(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})){3}$")
        if ipv4_validator.match(hostname):
            print("ok")
        else:
            print("error")
            return
        api = shodan.Shodan(os.getenv("SHODAN_API"))
        host = api.host(hostname)
        await ctx.channel.send(f"IP Address location: Longitude: {host['longitude']} & Latitude: {host['latitude']} \n"
                               f"https://www.openstreetmap.org/?mlat={host['latitude']}&mlon={host['longitude']}&zoom=12")

    @run.error
    async def run_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Incorrect arguments entered | **!command_name - outcome:str - amount:int')


def setup(bot):
    bot.add_cog(OutilGeolocalisation(bot))
