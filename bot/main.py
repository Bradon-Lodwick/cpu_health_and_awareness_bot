# -*- coding: utf-8 -*-
""" This file is used to start the cpu health and awareness bot.

Explanation
-----------
* Sets up the bot using the bot token
* Imports all the commands from the command folder

Todo
----
"""

from discord.ext import commands
from bot.constants import command_prefix, description, extensions
from bot.secrets import token

# The object for the bot
bot = commands.Bot(command_prefix=command_prefix,  description=description)


@bot.event
async def on_ready():
    """ Prints out information when the bot is started.
    """

    print('------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------------')


if __name__ == "__main__":
    """ The main function for the bot, starts the bot and runs all of the commands in the command folder.
    """

    print("START COMMAND SETUP\n------------------------")
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    print("COMMAND SETUP COMPLETED.\n-------------------------")

    bot.run(token)
