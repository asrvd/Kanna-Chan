import discord
from discord.ext import commands
from petpetgif import petpet
from io import BytesIO

class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def headpat(self, ctx, mem: discord.User()):
        if mem == None:
            mem = ctx.author
        asset = mem.avatar_url_as(format='png')
        await asset.save('av.png')
        dest = BytesIO()
        petpet.make('av.png', dest)
        dest.seek(0)
        file = discord.File(dest, filename="pat.gif")
        emb = discord.Embed(description=f"`{mem.name.lower()}_pat`",color=0x2e69f2)
        emb.set_image(url="attachment://pat.gif")
        await ctx.send(embed=emb, file=file)

def setup(client):
    client.add_cog(Meme(client))
    print(">> Meme loaded")