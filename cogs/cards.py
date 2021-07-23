import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

class Cards(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def uwucard(self, ctx, mem: discord.User = None):
        kana = self.client.get_user(self.kana_id)
        if mem == None:
            mem = ctx.author
        bg = Image.open("./images/lob.png")
        asset = mem.avatar_url_as(size=256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data).convert('RGBA')
        pfp = pfp.resize((181, 201))
        bg.paste(pfp, (35, 121))
        bg.save("uwu.png")
        file = discord.File("uwu.png")
        embed = discord.Embed(description=f"{mem.mention} you make {ctx.author.mention} happy uwu.", color=0x2e69f2)
        embed.set_image(url="attachment://uwu.png")
        embed.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=embed, file=file)

    @commands.command()
    async def gaycard(self, ctx):
        kana = self.client.get_user(self.kana_id)
        bg = Image.open("./images/gay_card.png")
        font = ImageFont.truetype("./fonts/roboto.ttf", 32)
        auth = ctx.author
        asset = auth.avatar_url_as(size=256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data).convert('RGBA')
        pfp = pfp.resize((238, 238))
        nick = auth.display_name
        bg.paste(pfp, (76, 165))
        draw = ImageDraw.Draw(bg)
        draw.text((368, 193), nick, (0, 0, 0), font=font)
        bg.save("gay.png")
        file = discord.File("gay.png")
        embed = discord.Embed(description=f"{ctx.author.mention} Here is your verified Gay Card.", color=0x2e69f2)
        embed.set_image(url="attachment://gay.png")
        embed.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=embed, file=file)

    @commands.command()
    async def simpcard(self, ctx, *, simp):
        kana = self.client.get_user(self.kana_id)
        bg = Image.open("./images/s.png")
        font = ImageFont.truetype("./fonts/roboto.ttf", 24)
        auth = ctx.author
        asset = auth.avatar_url_as(size=256)
        data = BytesIO(await asset.read())
        pfp = Image.open(data).convert('RGBA')
        pfp = pfp.resize((185, 214))
        nick = auth.display_name
        text = simp
        bg.paste(pfp, (47, 60))
        draw = ImageDraw.Draw(bg)
        draw.text((395, 172), nick, (0, 0, 0), font=font)
        draw.text((51, 349), text, (0, 0, 0), font=font)
        bg.save("simp.png")
        file = discord.File("simp.png")
        embed = discord.Embed(description=f"{ctx.author.mention} Here is your verified Simp Card.", color=0x2e69f2)
        embed.set_image(url="attachment://simp.png")
        embed.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=embed, file=file)

def setup(client):
    client.add_cog(Cards(client))
    print(">> Cards loaded")