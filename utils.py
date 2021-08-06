from discord.ext.commands.errors import BadArgument
from discord import Permissions


def to_lower(argument):  # Converts string or a list to lowercase
    if argument.isdigit():
        raise BadArgument
    if isinstance(argument, str):
        return argument.lower()
    elif isinstance(argument, list):
        return [arg.lower() for arg in argument]


def administrator_permissions():
    permissions = Permissions()
    permissions.update(administrator=True)
    return permissions
