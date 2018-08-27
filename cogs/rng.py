from discord.ext import commands

import string
import random
from random import randint as ri


class RNG():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random_string(self, ctx):
        await ctx.send(''.join([random.choice(string.printable) for f in range(ri(10, 44))]))

    # this was just a test, better version coming soon:tm:
    @commands.command()
    async def broll(self, ctx, die=20, mod=0, *args):
        roll = f'{random.randint(1, die)} + {mod}'
        if args:
            commenti = ' '.join(args)
            content = f'{roll} = {eval(roll)}, {comment}'
        else:
            content = f'{roll} = {eval(roll)}'
        await ctx.send(content)


def setup(bot):
    bot.add_cog(RNG(bot))
