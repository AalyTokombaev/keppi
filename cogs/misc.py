from discord.ext import commands

class Misc:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def get_messages(self, ctx, amt=0):
        x = 0
        async for message in ctx.message.channel.history(limit=0):
            x += 1
        await ctx.send(f'Found {x} messages')

def setup(bot):
    bot.add_cog(Misc(bot))