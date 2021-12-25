import discord
from discord.ext import commands
import random
import asyncio

class Highlow(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command(aliases=['gmn'])
  async def guess_my_number(self, ctx):
    #num1 is the number shown to the user
    num1 = random.randint(1, 100)
    #num2 is the number not shown to the user
    num2 = random.randint(1, 100)
    await ctx.send(f"{ctx.message.author.mention} I chose a number between 1 and 100. Guess whether **"+str(num1)+"** is higher, lower, or the same number. Respond with **higher**, **lower**, or **same**.")
    try:
      msg = await self.client.wait_for('message', timeout=15)
      def check(message):
        return message.content == ""
    except asyncio.TimeoutError:
      await ctx.send(f"{ctx.message.author.mention} You didn't type 'higher', 'lower', or 'same' in 15 seconds. Try again and be quicker!")
      return
    
    if msg.content == "higher":
      if num2 > num1:
        await ctx.send("Correct! You win! <:Trophy:858058617857114122>")
        return
      else:
        await ctx.send("Incorect! You lose! The correct number was **"+str(num2)+"**.")
        return
    if msg.content == "lower":
      if num2 < num1:
        await ctx.send("Correct! You win! <:Trophy:856751500080709642>")
        return
      else:
        await ctx.send9("Incorrect! You lose! The correct number was **"+str(num2)+"**.")
        return
    if msg.content == "same":
      if num2 == num1:
        await ctx.send("Correct! You win! <:Trophy:856751500080709642>")
        return
      else:
        await ctx.send("Incorrect! You lose! The correct number was **"+str(num2)+"**.")
        return
    else:
      await ctx.send("Error! You typed something that isn't 'higher', 'lower', or 'same'!")
      return
  
def setup(client):
  client.add_cog(Highlow(client))