import discord
from discord.ext import commands
import random
from random import randint
import time
prefix = "~"
#Place the channel ID which you want Sleepy Joe to speak in, here:
channelvar = ""
bot = commands.Bot(command_prefix=prefix)
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Build Back Better."))
    print("Inaugurated!")
    file = open('bidenquotes.txt', 'r')
    quotesline = file.readlines()
    linelist = []
    for line in quotesline:
        linelist.append(line.strip("\n"))
    while True:
        channel = bot.get_channel(channelvar)
        await channel.send(random.choice(linelist))
        randomtime = randint(1,10800)
        time.sleep(randomtime)
bot.run("")
