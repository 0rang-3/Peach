import discord
from discord.ext import commands

class Help(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def help(self, ctx, args=None):
    if args == None:
      embed = discord.Embed(title="🍑 Peach Help Menu", description="To choose a category, type: `;help <category>`", color=0xe38b10)
      
      embed.add_field(name="Games", value="All the Games that Peach has!")
      embed.set_footer(text="Made by: _Ven0m#4019 and Mihirsur007#7149")
      await ctx.send(embed=embed)
      return
    if args == "games":
      embed = discord.Embed(title="Games Help Menu", description="Yay! Games!", color=0x1df032)
      #changed the rocket league command from ;rocket_league to ;rl . Delete this comment when you have read it.
      embed.add_field(name="Rocket League", value="This game allows you to play Rocket League in Discord! It works on the first goal basis (first to score wins)! Type: `;rl`")
      embed.add_field(name="Guess My Number", value="Guess My Number chooses 2 numbers and tells you only 1. You need to guess whether the number you know is higher, lower, or the same as the secret number! Type: `;guess_my_number`")
      embed.add_field(name="Mario", value="Play Mario inside discord! (*original mario created and owned by nintendo*) Type: `;mario`")
      embed.add_field(name="Tic-Tac-Toe", value="Play Tic-Tac_Toe with your friends on discord! Type: `;tictactoe start @<player2>`")
      await ctx.send(embed=embed)
      
  
def setup(client):
  client.add_cog(Help(client))