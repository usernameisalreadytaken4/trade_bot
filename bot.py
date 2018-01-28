#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Roman B.

from urllib.parse import urlencode
from discord.ext.commands import Bot

import discord
import secrets


trade_bot = Bot(command_prefix="/")


@trade_bot.event
async def on_message(message):
    # do some extra stuff here

    return await trade_bot.process_commands(message)


@trade_bot.command()
async def sage(*args):
    url = ("http://www.sageadvice.eu/?{}".format(
               urlencode({'s': ' '.join(args)})
            ))
    return await trade_bot.say(url)


@trade_bot.command()
async def srd(*args):
    url = ("https://dnd5e.info/search.php?{}".format(
               urlencode({'zoom_query': ' '.join(args)})
            ))
    return await trade_bot.say(url)


@trade_bot.group(pass_context=True)
async def roll(ctx, *args: str):
    member = ctx.message.author
    await trade_bot.say('{}: {}'.format(member.mention, 'здесь был раньше roll'))


@trade_bot.group(pass_context=True)
async def r(ctx, *args: str):
    member = ctx.message.author
    await trade_bot.say('{}: {}'.format(member.mention, 'а здесь  было еще кто то, тот же ролл но через r'))


if __name__ == '__main__':
    trade_bot.run(secrets.BOT_TOKEN)


