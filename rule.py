from discord.ext import commands

class Rules(commands.Cog):
  def __init__(self, client):
    self.client = client

  f = open("rules.txt", 'r')
  rules = f.readlines()

  @commands.command(aliases=['rules'])
  async def rule(self, ctx, *, number):
    try:
      number = int(number)
      if int(number) > len(self.rules):
        await ctx.send("Rule Doesnt Exist !")
      else:
        await ctx.send(self.rules[int(number) - 1])
    except:
      await ctx.send("Please Enter A valid Number !")

def setup(client):
  client.add_cog(Rules(client))