import discord
from discord.ext import commands
from discord_components import Button
import asyncio

def get_embed(author, arg):
    if type(arg) != discord.User:
        arg = arg.capitalize()
    elif type(arg) == discord.User:
        arg = arg.mention
    embed = discord.Embed(color=0x2e69f2)
    embed.set_author(
        name=f"Press F to pay your respect to {arg}",
        icon_url=author.avatar_url
    )
    return embed

class F(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def f(self, ctx, *, user:str or discord.User):
        cm = [Button(style=1, label="Pay Respect", emoji="🇫")]
        cmd = [Button(style=1, label="Pay Respect", emoji="🇫", disabled=True)]
        emb = get_embed(ctx.author, user)
        msg = await ctx.send(embed=emb, components=cm)
        check_list = []
        while True:
            try:
                def check(resp):
                    return resp.channel == ctx.channel and resp.user not in check_list
                resp = await self.client.wait_for("button_click", check=check, timeout=15)
                check_list.append(resp.user)
                await resp.respond(type=4, ephemeral=False, content=f"**{resp.user.name.capitalize}** has paid their respect.")
            except asyncio.TimeoutError:
                await msg.edit(components=cmd)
                await ctx.send(f"{len(check_list)} users paid their respect.")
                check_list.clear()
                break

def setup(client):
  client.add_cog(F(client))
  print(">> Pay Respect loaded")
