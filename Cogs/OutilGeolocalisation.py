from discord.ext import commands
from dotenv import load_dotenv
import shodan
import os
import re


class OutilGeolocalisation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        load_dotenv(dotenv_path="config")

    # defines the actual command
    @commands.command(name="ip",
                      description="Cette commande géolocalise l'adresse IP donnée. Utilisation: !ip ip_address")
    async def run(self, ctx: commands.Context, hostname):
        # regex to validate the ip address
        ipv4_validator = re.compile(r"^(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})(?:\.(?:25[0-5]|2[0-4]\d|[0-1]?\d{1,2})){3}$")

        # triggers error on the discord channel if the ip address is not valid
        if not ipv4_validator.match(hostname):
            await ctx.channel.send("Error: please enter a correct ip address.")
            return

        # get the ip information from shodan
        api = shodan.Shodan(os.getenv("SHODAN_API"))
        host = api.host(hostname)

        # sends back the result to the discord channel
        await ctx.channel.send(f"IP Address location: Longitude: {host['longitude']} & Latitude: {host['latitude']} \n"
                               f"https://www.openstreetmap.org/?mlat="
                               f"{host['latitude']}&mlon={host['longitude']}&zoom=12")

    # error triggered on incorrect command formatting
    @run.error
    async def run_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Incorrect arguments entered | Usage : !ip ip_address')


# adds the commands to the bot
def setup(bot):
    bot.add_cog(OutilGeolocalisation(bot))
