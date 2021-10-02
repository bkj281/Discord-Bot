import os
import discord
import random
from discord import client
from dotenv import load_dotenv
from discord.ext import commands
import music
import tictactoe

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot('>')

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)

cogs2 = [tictactoe]

for i in range(len(cogs2)):
  cogs2[i].setup(client)

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	
	for guild in client.guilds:
		print(guild.name)
		# members = '\n - '.join([member.name for member in guild.members])
		# print(f'Guild Members:\n - {members}')
		for channel in guild.text_channels:
			if str(channel) == "general":
				await channel.send('Bot is now Online!')
				await channel.send('https://tenor.com/view/thanos-im-here-brave-gif-12046780')

@client.command()
async def hi(ctx):
	await ctx.send('https://tenor.com/view/hello-there-baby-yoda-mandolorian-hello-gif-20136589')
	await ctx.send('How you doing?')

@client.command()
async def flip_a_coin(ctx):
	face = [0, 1, 0, 0, 0, 1, 1, 0, 1, 1]
	if random.choice(face) == 1:
		await ctx.send(file=discord.File('head.jpg'))
	else:
		await ctx.send(file=discord.File('tail.jpg'))


client.run(TOKEN)