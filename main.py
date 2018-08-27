from discord.ext.commands import Bot
import cogs
from cogs import deps
#from cogs import reddit


bot = Bot(command_prefix='?')


startup_extensions = ['rng', 'reddit_grabber', 'misc']

@bot.event
async def on_ready():
    print('Logged in as:')
    print(f'{bot.user.name} :: {bot.user.id}')


@bot.command()
async def load(ctx, extension : str):
    """Loads an extension from cogs."""
    try:
        bot.load_extension(extension)
    except (AttributeError, ImportError) as e:
        await ctx.send(f'```py\n{type(e).__name__}: {str(e)}\n```')
    await ctx.send(f'{extension} loaded.')


@bot.command()
async def unload(ctx, extension):
    """Unloas an extension from cogs"""
    bot.unload_extension(extension)
    await ctx.send(f'Unloaded {extension}')


if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(f'cogs.{extension}')
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Failed to load extension {extension} {exc}')

bot.run('MzMyODkyNDQ2OTg1ODE0MDI2.DWR5nQ.Z9kfMsw-yA9rrT9ZbnQjPK7rIyU')
#now to add some cogs
