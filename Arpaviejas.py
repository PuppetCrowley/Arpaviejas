import asyncio
from itertools import cycle
from dotenv import load_dotenv
from os import path, getenv, listdir, system, name
from aiohttp import ClientSession
from termcolor import colored

from discord import Intents, Activity, ActivityType
from discord.ext.commands import Bot, Context
from discord.ext.tasks import loop

load_dotenv(path.join('.', '.env'))  # Load data from the .env file

# Put your Bot Token here. (you can also put it as a .env variable)
BOT_TOKEN = ""


class Arpaviejas(Bot):
    def __init__(self, **kwargs):
        intents = Intents.default()
        intents.members = True
        super().__init__(command_prefix='!',
                         intents=intents,
                         help_command=None,
                         case_insensitive=True,
                         **kwargs)
        self._extensions = [x.replace('.py', '')
                            for x in listdir('cogs') if x.endswith('.py') and '__init__' not in x]
        self.load_extensions()
        self.session = ClientSession(loop=self.loop)
        self.status = cycle(
            [Activity(type=ActivityType.listening, name="Customize your own status here"), ])

    """ METHODS """

    def load_extensions(self, cogs: Context = None, path: str = 'cogs.'):
        '''Loads the default set of extensions or a seperate one if given'''
        for extension in cogs or self._extensions:
            try:
                self.load_extension(f'{path}{extension}')
                print(colored(f'Loaded cog: {extension}', 'green'))
            except Exception as e:
                print(colored(f'LoadError: {extension}\n'
                      f'{type(e).__name__}: {e}', 'red'))

    @classmethod
    async def setup(cls, **kwargs):
        bot = cls()
        try:
            await bot.start(getenv('BOT_TOKEN') or BOT_TOKEN, **kwargs)
        except KeyboardInterrupt:
            await bot.close()

    """ EVENTS """

    async def on_ready(self):
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
        self.change_status.start()

    async def on_guild_channel_create(self, channel):
        y = 0
        # Use the logic, the name of the spam channels and this conditional must be the same, or the bot won't work.
        if channel.name == "server-punkwned":
            while y < 15:
                # The spam message, you can use your own custom message.
                await channel.send("||@everyone|| Server Punkwned:\nhttps://discord.gg/FhJydrmbTz")
                y += 1

    async def on_command_completion(self, ctx: Context):
        print(
            colored(f"{ctx.command.name} command was invoked successfully", 'green'))

    """ LOOPS """

    @loop(minutes=2)  # Run every 2 minutes
    async def change_status(self):
        _activity = next(self.status)  # Get the next status
        # Change the bot's status
        await self.change_presence(activity=_activity)


if __name__ == '__main__':
    system('cls' if name == 'nt' else 'clear')
    print(colored('Bot starting...', 'yellow'))
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(Arpaviejas.setup())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(colored(e, 'red'))
