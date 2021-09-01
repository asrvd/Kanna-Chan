import discord
from discord.ext import commands
from PIL import Image, ImageDraw
from io import BytesIO
import requests
import json
import anime_images_api
import random

anime = anime_images_api.Anime_Images()

handholdgifs = [
    "https://i.pinimg.com/originals/47/d1/8b/47d18b56a850217a46b517da4325d132.gif",
    "https://media3.giphy.com/media/w7RGPBLGO8rjq/giphy.gif",
    "https://carnivorouslreviews.files.wordpress.com/2018/08/interlocking.gif",
    "https://c.tenor.com/rU3xZo2_jaIAAAAC/anime-hold.gif",
    "https://i.pinimg.com/originals/1b/d8/82/1bd88210e9121fc133d6d4f5c74dc436.gif",
    "https://c.tenor.com/k1GwEAtwFisAAAAC/hand-hold.gif",
    "https://i.pinimg.com/originals/0e/6f/52/0e6f524f25fbc80c666d6541822e2522.gif",
    "https://64.media.tumblr.com/ccbf4267ced07c31b10cc793fd68739e/tumblr_pl2oo7Lyvt1riwylc_540.gif",
    "https://i.pinimg.com/originals/9a/d2/13/9ad213d65d185ad28f23eb1d962fd702.gif",
    "https://i.pinimg.com/originals/f1/c1/0a/f1c10af3018241ecd34c30581f94c49e.gif",
    "https://64.media.tumblr.com/f186c5794414804c7e0a05b0cde389f7/a943f0088f9398e4-36/s1280x1920/2cb09785526635978b4e54bf54ef120168673d13.gif",
    "https://giffiles.alphacoders.com/109/109140.gif",
    "https://thumbs.gfycat.com/AridImperturbableCavy-size_restricted.gif"
]

bonk_gifs = [
    "https://i.gifer.com/FoFy.gif",
    "https://c.tenor.com/1T5bgBYtMgUAAAAC/head-hit-anime.gif",
    "https://i.gifer.com/B6ya.gif",
    "https://c.tenor.com/U6vSI52F4jwAAAAC/anime-hit.gif",
    "https://i.pinimg.com/originals/99/ea/48/99ea48ec7a3d63e77186302e8d85426e.gif",
    "https://media1.giphy.com/media/30lxTuJueXE7C/giphy.gif",
    "https://i.imgur.com/0IxjsfM.gif",
    "https://i.pinimg.com/originals/87/67/c0/8767c0aa7de40a48aaf916aab8bc13cc.gif",
    "https://c.tenor.com/31WOy2yRK3QAAAAC/chuunibyou-hit.gif",
    "https://i.imgur.com/DIAbFlT.gif",
    "https://64.media.tumblr.com/09cd8d36a573a91ac22dd7521a12dfc8/tumblr_pq8976Yawh1y0nwq1o1_540.gif",
    "https://i.imgur.com/yPR6IXK.gif"
]

high5gifs = [
    "https://c.tenor.com/JBBZ9mQntx8AAAAC/anime-high-five.gif",
    "https://c.tenor.com/Ajl4l3PWf8sAAAAC/high-five-anime.gif",
    "https://acegif.com/wp-content/gif/high-five-83.gif",
    "https://i.imgur.com/Pr1rEzX.gif",
    "https://thumbs.gfycat.com/BreakableMessyHarrierhawk-size_restricted.gif",
    "https://i.pinimg.com/originals/01/82/de/0182de50a5c4fcb7af42737913f663a8.gif",
    "https://thumbs.gfycat.com/MeekElementaryDove-size_restricted.gif",
    "https://media2.giphy.com/media/x58AS8I9DBRgA/giphy.gif",
    "https://i.imgur.com/MMr5SnV.gif",
    "https://i.imgur.com/RDfVi1u.gif",
    "https://i.gifer.com/WZgQ.gif",
    "https://c.tenor.com/TJs8RfplhWIAAAAC/naruto-shippuuden.gif"
]

def return_gif(arg):
    request = requests.get(f"https://nekos.life/api/v2/img/{arg}")
    rjson = json.loads(request.content)
    return rjson['url']

class Roleplay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, m: discord.Member = None):
        if m == None:
            await ctx.send("Please mention someone to hug!")
        elif m == ctx.author:
            await ctx.send(f"{ctx.author.mention} Do you need someone to hug..? I can hug you :)")
        emb = discord.Embed(description=f"{ctx.author.mention} hugs {m.mention} ~ awww", color=0x2e69f2)
        emb.set_image(url=return_gif("hug"))
        await ctx.send(embed=emb)
    
    @commands.command()
    async def punch(self, ctx, m: discord.Member = None):
        if m == None:
            await ctx.send("Please mention someone to punch!")
        elif m == ctx.author:
            await ctx.send(f"{ctx.author.mention} You want to punch yourself..? Are you sure..?")
        elif m == self.client.user.id:
            emb = discord.Embed(description=f"no u {ctx.author.mention}", color=0x2e69f2)
            emb.set_image(url="https://c.tenor.com/eaAbCBZy0PoAAAAS/reverse-nozumi.gif")
            await ctx.reply(embed=emb)
        emb = discord.Embed(description=f"{ctx.author.mention} punches {m.mention} ~ OwO", color=0x2e69f2)
        req = requests.get('https://shiro.gg/api/images/punch')
        rjson = json.loads(req.content)
        emb.set_image(url=rjson['url'])
        await ctx.send(embed=emb)

    @commands.command()
    async def kiss(self, ctx, m: discord.Member = None):
        if m == None:
            await ctx.send("Please mention someone to kiss!")
        elif m == ctx.author:
            await ctx.send(f"{ctx.author.mention} You want to kiss yourself ...? I can give you a kiss :)")
        emb = discord.Embed(description=f"{ctx.author.mention} kisses {m.mention} ~ cute", color=0x2e69f2)
        emb.set_image(url=return_gif("kiss"))
        await ctx.send(embed=emb)
    
    @commands.command()
    async def cuddle(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} cuddles {m.mention} ~ kyaaa!", color=0x2e69f2)
        emb.set_image(url=return_gif("cuddle"))
        await ctx.send(embed=emb)
    
    @commands.command()
    async def slap(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        elif m == self.client.user.id:
            emb = discord.Embed(description=f"no u {ctx.author.mention}", color=0x2e69f2)
            emb.set_image(url="https://c.tenor.com/eaAbCBZy0PoAAAAS/reverse-nozumi.gif")
            await ctx.reply(embed=emb)
        emb = discord.Embed(description=f"{ctx.author.mention} slaps {m.mention} ~ baakaah", color=0x2e69f2)
        emb.set_image(url=return_gif("slap"))
        await ctx.send(embed=emb)
    
    @commands.command()
    async def pout(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} pouts at {m.mention} ~ hmph", color=0x2e69f2)
        req = requests.get('https://shiro.gg/api/images/pout')
        rjson = json.loads(req.content)
        emb.set_image(url=rjson['url'])
        await ctx.send(embed=emb)

    @commands.command()
    async def smug(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} smugs at {m.mention} ~ blehh", color=0x2e69f2)
        emb.set_image(url=return_gif("smug"))
        await ctx.send(embed=emb)

    @commands.command()
    async def tickle(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        elif m == self.client.user.id:
            emb = discord.Embed(description=f"no u {ctx.author.mention}", color=0x2e69f2)
            emb.set_image(url="https://c.tenor.com/eaAbCBZy0PoAAAAS/reverse-nozumi.gif")
            await ctx.reply(embed=emb)
        emb = discord.Embed(description=f"{ctx.author.mention} tickles {m.mention} ~_~", color=0x2e69f2)
        emb.set_image(url=return_gif("tickle"))
        await ctx.send(embed=emb)

    @commands.command()
    async def kill(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} kills {m.mention} ~ RIP", color=0x2e69f2)
        emb.set_image(url=anime.get_sfw('kill'))
        await ctx.send(embed=emb)

    @commands.command()
    async def bonk(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} bonks {m.mention} ~ >.<", color=0x2e69f2)
        emb.set_image(url=random.choice(bonk_gifs))
        await ctx.send(embed=emb)

    @commands.command()
    async def high5(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} high fives {m.mention} ~ yoshh!", color=0x2e69f2)
        emb.set_image(url=random.choice(high5gifs))
        await ctx.send(embed=emb)

    @commands.command()
    async def nom(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} noms {m.mention} ~ nyaa!", color=0x2e69f2)
        req = requests.get('https://shiro.gg/api/images/nom')
        rjson = json.loads(req.content)
        emb.set_image(url=rjson['url'])
        await ctx.send(embed=emb)

    @commands.command(aliases=['boop'])
    async def poke(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} pokes {m.mention} ~ OwO", color=0x2e69f2)
        req = requests.get('https://shiro.gg/api/images/poke')
        rjson = json.loads(req.content)
        emb.set_image(url=rjson['url'])
        await ctx.send(embed=emb)

    @commands.command()
    async def blush(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} blushes at {m.mention} ~ >.<", color=0x2e69f2)
        req = requests.get('https://shiro.gg/api/images/blush')
        rjson = json.loads(req.content)
        emb.set_image(url=rjson['url'])
        await ctx.send(embed=emb)

    @commands.command(aliases=["hold"])
    async def handhold(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} holds {m.mention}'s hands ~ cutee", color=0x2e69f2)
        emb.set_image(url=random.choice(handholdgifs))
        await ctx.send(embed=emb)

    @commands.command()
    async def feed(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} feeds {m.mention} ~ uwu", color=0x2e69f2)
        emb.set_image(url=return_gif("feed"))
        await ctx.send(embed=emb)

    @commands.command()
    async def pat(self, ctx, m1: discord.Member = None, m2: discord.Member = None):
        if m1 == None:
            m1 = ctx.author
            m2 = ctx.author
        elif m2 == None:
            m2 = m1
            m1 = ctx.author
        
        bg = Image.open("./images/kanna_pat.png")
        asset1 = m1.avatar_url_as(format='png', size=128)
        asset2 = m2.avatar_url_as(format='png', size=128)
        await asset1.save('pfp1.png')
        await asset2.save('pfp2.png')
        pfp1 = Image.open('pfp1.png')
        pfp2 = Image.open('pfp2.png')
        pfp1 = pfp1.resize((122, 122))
        pfp2 = pfp2.resize((122, 122))
        mask = Image.new('L', (122, 122), 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0, 122, 122), fill=255)
        mask.save('mask.jpg')
        bgimg = bg.copy()
        bgimg.paste(pfp1, (122, 86), mask)
        bgimg.paste(pfp2, (355, 82), mask)

        bgimg.save("pat.png")
        file = discord.File("pat.png")
        emb = discord.Embed(title="", description=f"{m1.mention} pats {m2.mention} uwu", color=0x2e69f2)
        emb.set_image(url="attachment://pat.png")
        await ctx.send(embed=emb, file=file)

def setup(client):
    client.add_cog(Roleplay(client))
    print(">> Roleplay loaded")
