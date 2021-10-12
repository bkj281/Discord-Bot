import discord
from discord.ext import commands
import random

class Feature(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['c'])
  async def clear(self, ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

  @commands.command()
  async def flip_coin(self, ctx):
  	face = [0, 1, 0, 0, 0, 1, 1, 0, 1, 1]
  	if random.choice(face) == 1:
  		await ctx.send(file=discord.File('head.jpg'))
  	else:
  		await ctx.send(file=discord.File('tail.jpg'))
   
  @commands.command()
  async def hi(self, ctx):
    await ctx.send('https://tenor.com/view/hello-there-baby-yoda-mandolorian-hello-gif-20136589')
    em = discord.Embed(title="Howz you doing?", color=discord.Color.dark_teal())
    await ctx.send(embed=em)

  @commands.command(aliases=['k'])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="No Reason Provided"):
    try:
      await member.send("You Have Been Kicked From Our Community, Because: " + reason)
    except:
      await ctx.send("DM is Closed")
    await member.kick(reason=reason)

  @commands.command(aliases=['b'])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason="No Reason Provided"):
    await ctx.send("You Have Been Banned From Our Community, Because: " + reason)
    await member.ban(reason=reason)

  @commands.command(aliases=['ub'])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx,*, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
      user = banned_entry.user
			
      if (user.name, user.discriminator) == (member_name, member_disc):
        await ctx.guild.unban(user)
        await ctx.send(member_name + " has been unbanned!")
        return

    await ctx.send(member + " was not found")


  @commands.command(aliases=['m'])
  @commands.has_permissions(kick_members=True)
  async def mute(self, ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(894893906163036161)
    
    await member.add_roles(muted_role)
    
    await ctx.send(member.mention + " has been muted")


  @commands.command(aliases=['un'])
  @commands.has_permissions(kick_members=True)
  async def unmute(self, ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(894893906163036161)
    
    await member.remove_roles(muted_role)
    
    await ctx.send(member.mention + " has been unmuted")

  @commands.command(aliases=['user', 'info'])
  async def whois(self, ctx, member: discord.Member):
    embed = discord.Embed(title=member.name, description=member.mention, color=discord.Color.red())
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Requested By {ctx.author.name}")
    embed.add_field(name="Role", value=member.roles[1])
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Feature(client))