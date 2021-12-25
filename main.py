import discord
import os
from keep_alive import keep_alive
from discord.ext import commands, tasks
from discord.utils import get

client = discord.Client()
client = commands.Bot(command_prefix = ';')#Makes the bot prefix.
client.remove_command('help')#Removes buggy help command

#Notifies when bot is alive
@client.event
async def on_ready():
  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))

  await client.change_presence(activity=discord.Streaming(name=';help', url='https://www.youtube.com/watch?v=j5a0jTc9S10'))


@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')




"""
COGS REFERENCE

import discord
from discord.ext import commands

class Example(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def command(self, ctx):
    await ctx.send("Success")
  
def setup(client):
  client.add_cog(Example(client))
  
"""


keep_alive()
token = os.environ.get("DISCORD_TOKEN")
client.run(token)