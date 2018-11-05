# -*- coding: utf-8 -*-
""" This file contains all of the commands related to teams and team channels.
"""

from discord.ext import commands


class Teams:
    """ Commands that are used to setup or modify teams for the hackathon.
    """

    def __init__(self, bot):
        """ Constructs the Groups class, adding the commands to the given bot.

        Parameters
        ----------
        bot: discord.ext.commands.Bot
            The bot to have the commands added to.
        """

        # Sets the bot of the class to the given bot
        self.bot = bot

    @commands.command(pass_context=True)
    async def join_team(self, ctx):
        """ Adds the user to the given role, assuming the role has no extra permissions.
        """

        # The message that was sent
        message = ctx.message
        # The channel of the message
        channel = message.channel
        # The author of the message
        author = message.author

        # Check to make sure a role was mentioned
        if len(message.role_mentions) != 1:
            await channel.send(content="Please mention 1 and only 1 team role you would like to be added to using"
                                       "@team-name")
        # Check to make sure the role doesn't include admin privileges
        elif message.role_mentions[0].permissions.administrator:
            await channel.send(content="You can't add yourself to an administrator role!")
        # Check to make sure the user isn't already included in a team role (can only be apart of everyone)
        elif len(author.roles) != 1:
            print(len(author.roles))
            await channel.send(content="You are already apart of a team/are in a role. Please contact an admin if "
                                       "you think this is a mistake")
        # Actually add the role to the user
        else:
            await author.add_roles(message.role_mentions[0])
            await channel.send(content="Your role has been added, and you should be able to see your team's "
                                       "channels now!")


def setup(bot):
    """ Used to import the commands for use in the given bot.
    Parameters
    ----------
    bot : discord.ext.commands.Bot
        The bot to have the commands added to.
    """

    # Adds the commands to the bot
    bot.add_cog(Teams(bot))
