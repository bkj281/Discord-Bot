import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
from youtubesearchpython import VideosSearch

class Music(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def join(self, ctx):

    if ctx.author.voice is None:
      await ctx.send("Please join a voice channel first!!")

    voice_channel = ctx.author.voice.channel

    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

  @commands.command()
  async def leave(self, ctx):
    
    if ctx.voice_client is None:
      await ctx.send('Already Not Connected')
    else:
      await ctx.voice_client.disconnect()

  @commands.command()
  async def play(self, ctx, *string):
    
    if ctx.voice_client.is_playing():
      ctx.voice_client.stop()

    print(string)
    name = ''

    for i in string:
      name += i + " "

    FFMPEG_OPTIONS = { 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn' }
    
    videosSearch = VideosSearch(name, limit = 1)
    url = videosSearch.result()['result'][0]['link']
    print(url)

    ydl = YoutubeDL({'format':'bestaudio'})
    info = ydl.extract_info(url, download=False)
    url2 = info['formats'][0]['url']
    
    source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)

    ctx.voice_client.play(source)

  @commands.command()
  async def pause(self, ctx):
    
    if ctx.voice_client.is_playing():
      ctx.voice_client.pause()
      await ctx.send('Paused!')
    else:
      await ctx.send('Already Paused!')

  @commands.command()
  async def resume(self, ctx):
    
    if ctx.voice_client.is_playing():
      await ctx.send('Already Playing!')
    else:
      ctx.voice_client.resume()
      await ctx.send('Resumed!')

  @commands.command()
  async def stop(self, ctx):
    
    if ctx.voice_client.is_playing():
      ctx.voice_client.stop()
      await ctx.send('Stopped!')
    else:
      await ctx.send('Nothing Playing!')

def setup(client):
  client.add_cog(Music(client))