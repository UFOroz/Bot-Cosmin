import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')


@client.event
async def on_ready():
    print('Cosmin is ready!')

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f'Welcome to the server{member.mention}')


client.run('NjcwNjY1ODc2OTkwODUzMTcw.XixsWQ.1g4cjhqBL35pohqO4R58bLPB4B0')