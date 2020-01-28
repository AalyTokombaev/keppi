from discord.ext import commands
from string import ascii_letters

class Text():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def aesthetics(self, ctx, *args):
        message = ' '.join(args)
        new_message = ''.join([f'_`{v}`_' for v in message])

        await ctx.send(new_message)

    @commands.command()
    async def regionals(self, ctx, *args):
        message = ' '.join(args)
        new_message = ''.join([f':regional_indicator_{v}' if v in ascii_letters else ' ' for v in message])

        await ctx.send(new_message)


def setup(bot):
    bot.add_cog(Text(bot))
