import discord
import os
import random
from itertools import cycle

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

BOTS_LIST = ['ChoreBot', 'ChoreBot v2']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$assignchores'):
        real_members = [member for member in message.guild.members if member.name not in BOTS_LIST]
        random.shuffle(real_members)
        member_cycle = cycle(real_members)
        chores = open("chores.txt").readlines()
        random.shuffle(chores)

        for chore in chores:
            member = next(member_cycle)
            await message.channel.send(member.name + ' please ' + chore)

client.run(os.getenv('TOKEN'))