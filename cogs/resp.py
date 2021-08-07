import discord
import funresponses
from discord.ext import commands

class Response(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def simp(self, ctx, mem: discord.Member = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(titile="", description=f"{ctx.author.mention} simps on {mem.mention} <3\n*`{funresponses.pickup()}`*", color=0x2e69f2)
        emb.set_image(url="https://i.imgur.com/RlrlmmP.gif")
        await ctx.send(embed=emb)
        
def setup(client):
  client.add_cog(Response(client))
  print(">> Responses loaded")   