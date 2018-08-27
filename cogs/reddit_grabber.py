from discord.ext import commands
from .deps import reddit


class Vars:
    memes = reddit.dankmemes


class RedditImages(Vars):
    def __init__(self, bot):
        self.bot = bot
   
    
    @commands.command(pass_context=True)
    async def dankmeme(self, ctx):
        await ctx.send(self.memes.get_image())


    @commands.command(pass_context=True)
    async def test_reddit(self, ctx):
        await ctx.send('hello, this is reddit')
        



def setup(bot):
    bot.add_cog(RedditImages(bot))


