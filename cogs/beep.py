import discord
import time
from discord.ext import commands

class Beep(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def beep(self, ctx, member : discord.Member=None):
    if member == None:
      who_to_mention = ctx.message.author
    else:
      who_to_mention = member
    for x in range(1, 2):
      await ctx.send(f"{who_to_mention.mention} beep")
      time.sleep(0.2)
      await ctx.send(f"{who_to_mention.mention} beep")
      time.sleep(0.2)
      await ctx.send(f"{who_to_mention.mention} ur")
      time.sleep(0.1)
      await ctx.send(f"{who_to_mention.mention} a")
      
      await ctx.send(f"{who_to_mention.mention} sheep")

      await ctx.send(f"{who_to_mention.mention} beep")

      await ctx.send(f"{who_to_mention.mention} beep")

      await ctx.send(f"{who_to_mention.mention} ur")

      await ctx.send(f"{who_to_mention.mention} a")

      await ctx.send(f"{who_to_mention.mention} sheep")


  
def setup(client):
  client.add_cog(Beep(client))