import discord

from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!hi'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)  # This line is needed to process commands

bot.run('MTEyMDA5NzQ0MjIzMTIzNDU3Mw.GxQOnr.9FMrLd6LAdFmsNE2bLtUjHmju3TPjFBC3iQzis')
