import os
import discord
from discord.ext import commands
from decouple import config

intents = discord.Intents.default()
intents.members = True
intents.presences = True

kana_id = 857835279259664403
client = commands.Bot(command_prefix=['kanna ', 'kana ', 'k.', 'K.', 'Kanna ', 'Kana '], case_insensitive=True, intents=intents)
client.remove_command("help")

def load_cogs():
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.load_extension(f"cogs.{file[:-3]}")

print(">> Kanna is awaking...")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name='Asheeshh Onii Chan'))
  load_cogs()
  print(">> Cogs loaded.")
  print('>> Kanna is Online.')

@client.command()
@commands.is_owner()
async def reload(ctx):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.reload_extension(f"cogs.{file[:-3]}")
  await ctx.send("```>> Kanna reloaded cogs```")

token = config("TOKEN")
client.run(token)

