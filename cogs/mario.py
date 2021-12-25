import discord
import time
from discord.ext import commands
import asyncio

class Mario(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def mario(self, ctx):
    #START CODING HERE
    await ctx.send("─▄████▄▄░")
    await ctx.send("▄▀█▀▐└─┐░░")
    await ctx.send("█▄▐▌▄█▄┘██")
    await ctx.send("└▄▄▄▄▄┘███")
    await ctx.send("██▒█▒███▀")
    await ctx.send("🄼🄰🅁🄸🄾"'')
    await ctx.send("<:MarioCoin:856999129480560697> **type ;play_mario to play** <:MarioCoin:856999129480560697>")

  @commands.command()
  async def play_mario(self, ctx):
    #START CODING HERE
    embed = discord.Embed (title = "<a:AnimatedMario:856962594807742544> Mario Menu", description = "All of mario's games")
    embed.add_field(name = "***LEVEL 1***", value = "*Type ;play_lvl_1*" )
    embed.add_field(name = "***LEVEL 2***", value = "*Type ;play_lvl_2*" )
    await ctx.send(embed=embed)
    #level 1
  @commands.command()
  async def play_lvl_1(self, ctx):
    #START CODING HERE
    await ctx.send("*here is a quick tutorial*")
    time.sleep(2)
    await ctx.send("*each square is 1 block, and the yellow areas are the paths*")
    time.sleep(5)
    await ctx.send("this is a top down view of the map, so the to move from the bottom of the picture to the top is moving forward.")
    time.sleep(5)
    await ctx.send("to move forward type `forward`. to turn left or right type `left` or `right`. To go backwards type `backward` in between each command, add `,` (no spaces).  ")
    time.sleep(8)
    await ctx.send("here is an example: if you had to move forward 2 blocks, turn right, and move towards the right 3 blocks, you would type ` forward,forward,right,right,right` ")
    time.sleep(15)
    await ctx.send("course 1:   ")
    await ctx.send("https://lh3.googleusercontent.com/pMRyPB1SJoYZd31xxZ__TMco04sXymHvO50MWBALKffx5h5p4BO57m4UKGc9lM2e3itc5XiiPwm5lAj3ztgdjAXy4_AJeB-0hV9yz-qdz_aOp6vSWlEYOiPdr7ZF4HvTWDDTsHBDHg=w2400")
    #level 1 answer
    await ctx.send(f"{ctx.message.author.mention} Type the answer here:  ")
    try:
      msg = await self.client.wait_for('message', timeout=60)
      def check(message):
        return message.content == ""
    except asyncio.TimeoutError:
      await ctx.send(f"{ctx.message.author.mention} You didn't type the answer in 60 seconds. Try again and be quicker!")
      return

    if msg.content == ("forward,forward,right,right,forward,right,right,forward,forward,forward"):
      await ctx.send("Correct! <:MarioCoin:856999129480560697> <:Trophy:858058617857114122>")
    else:
      await ctx.send("Oh no! You stepped on a goomba and it **yeeted** you into the void. Try again! (go back to the menu `;play_mario`")
      await ctx.send("https://lh3.googleusercontent.com/sNlG3hr3mdWYra_k4Yqx0PZZmMHEeUHAsB_KFtz1Q-JLOQq3oDCqPdESgmyW6tle02opT7MdJnFf5C03t4lr_46tpGcJagucRGUcSv3ozZ34OJ3m9xOCJ6mYP8UWE_xbkYyoz8tGHw=w2400")
  #level 2
  @commands.command()
  async def play_lvl_2(self, ctx):
    await ctx.send("course 2:   ")
    await ctx.send("https://lh3.googleusercontent.com/pZU9eqXM9hhBXBx_p2nhJ82HS736CIia53uK_yowH6A7NMAGC7ea9eMALdZu0ZmD_SsZZBYX1Jh-yx9FPsh6CGo8lhQlQHErqz-qRjMA1Kw1OjBeE7W0GgD3G0tHCirdb2fvAXBNSQ=w2400")
    #level 2 answer
    await ctx.send(f"{ctx.message.author.mention} Type the answer here:  ")
    try:
      msg = await self.client.wait_for('message', timeout=60)
      def check(message):
        return message.content == ""
    except asyncio.TimeoutError:
      await ctx.send(f"{ctx.message.author.mention} You didn't type the answer in 60 seconds. Try again and be quicker!")
      return

    if msg.content == ("forward,forward,forward,forward,forward,left,left,backward,backward,left,left,left,forward,forward,forward"):
      await ctx.send("Correct! <:MarioCoin:856999129480560697> <:Trophy:858058617857114122>")
    else:
      await ctx.send("Oh no! You stepped on a goomba and it **yeeted** you into the void. Try again! (go back to the menu `;play_mario`")
      await ctx.send("https://lh3.googleusercontent.com/sNlG3hr3mdWYra_k4Yqx0PZZmMHEeUHAsB_KFtz1Q-JLOQq3oDCqPdESgmyW6tle02opT7MdJnFf5C03t4lr_46tpGcJagucRGUcSv3ozZ34OJ3m9xOCJ6mYP8UWE_xbkYyoz8tGHw=w2400")

def setup(client):
  client.add_cog(Mario(client))