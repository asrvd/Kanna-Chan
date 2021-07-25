from akinator.async_aki import Akinator
import akinator
import asyncio
import discord
from discord.ext import commands

aki = Akinator()

class Akinator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def akinator(self, ctx):
        await ctx.author.send(f"{ctx.author.mention} The game is about to begin!\n You will get 60 seconds to answer each question, answer in `yes/no` or `y/n`.")
        await asyncio.sleep(5)
        q = await aki.start_game()
        c = 0
        while aki.progression <= 80:
            await ctx.author.send(f"**{q}**")
            try:
                def check(m):
                    return m.author == ctx.author and m.channel.type is discord.ChannelType.private
                a = await self.client.wait_for('message', check=check, timeout=60)
                if a == "back":
                    try:
                        q = await aki.back()
                    except akinator.CantGoBackAnyFurther:
                        pass
                elif a == "stop":
                    await aki.close()
                    await ctx.author.send(f"{ctx.author.mention} Game stopped!")
                    c = c+1
                    break
                else:
                    try:
                        q = await aki.answer(a.content.lower())
                    except Exception:
                        await ctx.author.send("Invalid Response to question!\nAnswer in `yes/no` or `y/n`.")
            except asyncio.TimeoutError:
                await ctx.author.send(f"{ctx.author.mention} You took too long to answer the question, the game has been stopped!")
                await aki.close()
                c = c+1
                break
        await aki.win()

        if c == 0:
            desc=f"**It's {aki.first_guess['name']}**\n*{aki.first_guess['description']}*!\n**Was I correct? (yes/no)**"
            emb = discord.Embed(title="Here is my guess!", description=desc)
            emb.set_image(url=aki.first_guess['absolute_picture_path'])
            await ctx.author.send(embed=emb)
            def check(m):
                    return m.author == ctx.author
            correct = await self.client.wait_for('message', check=check, timeout=60)
            if correct.content.lower() == "yes" or correct.content.lower() == "y":
                await ctx.author.send("Yay :)")
            else:
                await ctx.author.send("Oof :(")
            await aki.close()

def setup(client):
  client.add_cog(Akinator(client))
  print(">> Akinator loaded")