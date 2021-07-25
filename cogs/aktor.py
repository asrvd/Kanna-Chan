from akinator.async_aki import Akinator
import akinator
import asyncio
import discord
from discord.ext import commands
import pyrebase
import json
from decouple import config

aki = Akinator()
firebase = pyrebase.initialize_app(json.loads(config("firebaseConfig")))
db = firebase.database()

def create(guild, channel):
    db.child("AKINATOR").child(guild).set({"CHANNEL": channel})

def check_channel(guild, channel):
    ch = db.child("AKINATOR").child(guild).child("CHANNEL").get().val()
    if ch == channel:
        return True
    elif ch == None:
        return "None"
    else:
        return False

class Akinator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def aksetup(self, ctx, *, channel: discord.TextChannel = None):
        if channel != None:
            create(ctx.message.guild.id, channel.id)
            await ctx.send(f"Akinator has been setup to {channel.mention}")
        else:
            await ctx.send("You need to mention a channel!")

    @commands.command()
    async def akinator(self, ctx):
        if check_channel(ctx.message.guild.id, ctx.message.channel.id) == True:
            await ctx.send(f"{ctx.author.mention} The game is about to begin!\n You will get 60 seconds to answer each question, answer in `yes/no` or `y/n`.")
            await asyncio.sleep(5)
            q = await aki.start_game()
            c = 0
            while aki.progression <= 80:
                await ctx.send(f"**{q}**")
                try:
                    def check(m):
                        return m.author == ctx.author
                    a = await self.client.wait_for('message', check=check, timeout=60)
                    if a == "back":
                        try:
                            q = await aki.back()
                        except akinator.CantGoBackAnyFurther:
                            pass
                    elif a == "stop":
                        await aki.close()
                        await ctx.send(f"{ctx.author.mention} Game stopped!")
                        c = c+1
                        break
                    else:
                        try:
                            q = await aki.answer(a.content.lower())
                        except Exception:
                            await ctx.send("Invalid Response to question!\nAnswer in `yes/no` or `y/n`.")
                except asyncio.TimeoutError:
                    await ctx.send(f"{ctx.author.mention} You took too long to answer the question, the game has been stopped!")
                    await aki.close()
                    c = c+1
                    break
            await aki.win()

            if c == 0:
                desc=f"**It's {aki.first_guess['name']}**\n*{aki.first_guess['description']}*!\n**Was I correct? (yes/no)**"
                emb = discord.Embed(title="Here is my guess!", description=desc)
                emb.set_image(url=aki.first_guess['absolute_picture_path'])
                await ctx.send(embed=emb)
                def check(m):
                    return m.author == ctx.author
                correct = await self.client.wait_for('message', check=check, timeout=60)
                if correct.content.lower() == "yes" or correct.content.lower() == "y":
                    await ctx.send("Yay :)")
                else:
                    await ctx.send("Oof :(")
                await aki.close()
        elif check_channel(ctx.message.guild.id, ctx.message.channel.id) == "None":
            await ctx.send("No channel is set for akinator!\nUse `kana aksetup` to setup channel.")
        else:
            await ctx.send("This command cannot be run in this channel!")

def setup(client):
  client.add_cog(Akinator(client))
  print(">> Akinator loaded")