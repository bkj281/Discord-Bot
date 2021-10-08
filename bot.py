import os
import discord
import random
from discord import client
from dotenv import load_dotenv
from discord.ext import commands
import music
import feature
import rule

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot('>')
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
	em = discord.Embed(title="Help", description="Use >Help <command> for More Information",
	                         color=discord.Color.orange())

	em.add_field(name="Moderation", value="kick, ban, mute, whois")
	em.add_field(name="Game", value="tictactoe, flip_coin")
	em.add_field(name="Music", value="play, pause, stop, resume, join, leave")
	await ctx.send(embed=em)

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)

cogs2 = [feature]

for i in range(len(cogs2)):
  cogs2[i].setup(client)

cogs3 = [rule]

for i in range(len(cogs3)):
  cogs3[i].setup(client)


@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')

	await client.change_presence(status=discord.Status.idle, activity=discord.Game('Let\'s Enjoy'))
	
	for guild in client.guilds:
		print(guild.name)
		# members = '\n - '.join([member.name for member in guild.members])
		# print(f'Guild Members:\n - {members}')
		for channel in guild.text_channels:
			if str(channel) == "general":
				await channel.send('Bot is now Online!')
				await channel.send('https://tenor.com/view/thanos-im-here-brave-gif-12046780')

@client.event
async def on_message(msg):
  filtered_words = ["sad", "unhappy"]
  for word in filtered_words:
    if word in msg.content:
      await msg.delete()
  await client.process_commands(msg)


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("Invalid Command !")
    await ctx.message.delete()
    await ctx.send("Use >Help for List of Commands")


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]


@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
  global count
  global player1
  global player2
  global turn
  global gameOver

  if gameOver:
    global board
    board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
             ":white_large_square:", ":white_large_square:", ":white_large_square:",
             ":white_large_square:", ":white_large_square:", ":white_large_square:"]
    turn = ""
    gameOver = False
    count = 0

    player1 = p1
    player2 = p2

    # print the board
    line = ""
    for x in range(len(board)):
        if x == 2 or x == 5 or x == 8:
            line += " " + board[x]
            await ctx.send(line)
            line = ""
        else:
            line += " " + board[x]

    # determine who goes first
    num = random.randint(1, 2)
    if num == 1:
        turn = player1
        await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
    elif num == 2:
        turn = player2
        await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
  else:
    await ctx.send("A game is already in progress! Finish it before starting a new one.")


@client.command()
async def place(ctx, pos: int):
  global turn
  global player1
  global player2
  global board
  global count
  global gameOver

  if not gameOver:
    mark = ""
    if turn == ctx.author:
      if turn == player1:
        mark = ":regional_indicator_x:"
      elif turn == player2:
        mark = ":o2:"
      if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
        board[pos - 1] = mark
        count += 1

        # print the board
        line = ""
        for x in range(len(board)):
          if x == 2 or x == 5 or x == 8:
            line += " " + board[x]
            await ctx.send(line)
            line = ""
          else:
            line += " " + board[x]

        checkWinner(winningConditions, mark)
        print(count)
        if gameOver == True:
          await ctx.send(mark + " wins!")
        elif count >= 9:
          gameOver = True
          await ctx.send("It's a tie!")
        # switch turns
        if turn == player1:
          turn = player2
        elif turn == player2:
          turn = player1
      else:
        await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
    else:
      await ctx.send("It is not your turn.")
  else:
    await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
  global gameOver
  for condition in winningConditions:
    if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
      gameOver = True


@tictactoe.error
async def tictactoe_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention 2 players for this command.")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")


@place.error
async def place_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please enter a position you would like to mark.")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please make sure to enter an integer.")

client.run(TOKEN)
