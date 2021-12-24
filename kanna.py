import os
import discord
from discord.ext import commands, tasks
from decouple import config
from discord_components import DiscordComponents
import asyncio
import random

intents = discord.Intents.default()
intents.members = True

#kana variables
kana_id = 857835279259664403
client = commands.Bot(command_prefix=commands.when_mentioned_or('kanna ', 'kana ', 'k.', 'K.', 'Kanna ', 'Kana '), case_insensitive=True, intents=intents)
client.remove_command("help")

print(">> Kanna is awaking...")

def load_cogs():
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.load_extension(f"cogs.{file[:-3]}")

@tasks.loop(seconds=10)
async def switchpresence():
  await client.wait_until_ready()
  #sm = [f"{len(client.guilds)} Servers!", f"{len(client.users)} Users!"]
  ch = ["Christmas Carols", "Snowfall", "Cold December Night", "小林さんちのメイドラゴン"]
  #ast = random.choice(sm)
  await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name=random.choice(ch), url="https://twitch.tv/asheeeshh"))

@client.event
async def on_ready():
  load_cogs()
  DiscordComponents(client)
  print(">> Cogs loaded.")
  print(f">> Logged in as : {client.user.name} \n>> ID : {client.user.id}")
  print(f">> Total Servers : {len(client.guilds)}")
  print('>> Kanna is Online.')

@client.command()
@commands.is_owner()
async def unload(ctx, *,extension):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.unload_extension(f"cogs.{extension}")
  await ctx.send(f"```>> Kanna unloaded {extension}```")
  
@client.command()
@commands.is_owner()
async def load(ctx, *,extension):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.load_extension(f"cogs.{extension}")
  await ctx.send(f"```>> Kanna unloaded {extension}```")

@client.command()
@commands.is_owner()
async def reload(ctx):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.reload_extension(f"cogs.{file[:-3]}")
  await ctx.send("```>> Kanna reloaded cogs```")

token = config("TOKEN")
switchpresence.start()
client.run(token)

