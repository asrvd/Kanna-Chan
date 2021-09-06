import discord
import funresponses
from discord.ext import commands
import random
from decouple import config
import requests
import json

API_KEY = config("WEEBY_API_KEY")

simp_gifs = [
    "https://i.imgur.com/RlrlmmP.gif",
    "https://c.tenor.com/nOARJZENR9UAAAAS/anime-in-love.gif",
    "https://c.tenor.com/hCqcNUuWCf0AAAAS/blush-anime.gif",
    "https://c.tenor.com/u1H1QTx8sxIAAAAC/anime-in-love.gif",
    "https://c.tenor.com/RzmW-BtosV4AAAAS/show-by-rock-cyan-hijirikawa.gif",
    "https://c.tenor.com/xc7x66o3rPUAAAAS/anime-love-anime.gif"
]

class Response(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def simp(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(titile="", description=f"{ctx.author.mention} simps on {mem.mention} <3\n\n*`{funresponses.pickup()}`*", color=0x2e69f2)
        emb.set_image(url=f"{random.choice(simp_gifs)}")
        await ctx.send(embed=emb)
    
    @commands.command()
    async def roast(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        req = requests.get(f"https://weebyapi.xyz/json/roast?token={str(API_KEY)}")
        js = json.loads(req.content)
        await ctx.send(f"{mem.mention}\n{js['response']}")
    
        
def setup(client):
  client.add_cog(Response(client))
  print(">> Responses loaded")   
