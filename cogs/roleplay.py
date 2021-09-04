import discord
from discord.ext import commands
from PIL import Image, ImageDraw
from io import BytesIO
import requests
import json
import random
from decouple import config

API_KEY = config("WEEBY_API_KEY")

def return_gif(arg):
    request = requests.get(f"https://weebyapi.xyz/gif/{arg}?token={str(API_KEY)}")
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
        else:
            emb = discord.Embed(description=f"{ctx.author.mention} hugs {m.mention} ~ awww", color=0x2e69f2)
            emb.set_image(url=return_gif("hug"))
            await ctx.send(embed=emb)
    
    @commands.command()
    async def punch(self, ctx, m: discord.Member = None):
        if m == None:
            await ctx.send("Please mention someone to punch!")
        elif m == ctx.author:
            await ctx.send(f"{ctx.author.mention} You want to punch yourself..? Are you sure..?")
        elif m.id == self.client.user.id:
            emb = discord.Embed(description=f"no u {ctx.author.mention}", color=0x2e69f2)
            emb.set_image(url="https://c.tenor.com/eaAbCBZy0PoAAAAS/reverse-nozumi.gif")
            await ctx.reply(embed=emb)
        else:
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
        if m == ctx.author:
            await ctx.reply("aww, you want a cuddle? I can give you a cuddle :)")
        elif m == None:
            await ctx.reply("Please `mention` someone to cuddle!")
        else:
            emb = discord.Embed(description=f"{ctx.author.mention} cuddles {m.mention} ~ kyaaa!", color=0x2e69f2)
            emb.set_image(url=return_gif("cuddle"))
            await ctx.send(embed=emb)
    
    @commands.command()
    async def slap(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        else:
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
        emb = discord.Embed(description=f"{ctx.author.mention} tickles {m.mention} ~_~", color=0x2e69f2)
        emb.set_image(url=return_gif("tickle"))
        await ctx.send(embed=emb)

    @commands.command()
    async def kill(self, ctx, m: discord.Member = None):
        if m == None:
            await ctx.reply("Who do you want to `kill`?")
        else:
            emb = discord.Embed(description=f"{ctx.author.mention} kills {m.mention} ~ RIP", color=0x2e69f2)
            emb.set_image(url=return_gif("kill"))
            await ctx.send(embed=emb)

    @commands.command()
    async def bonk(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} bonks {m.mention} ~ >.<", color=0x2e69f2)
        emb.set_image(url=return_gif("bonk"))
        await ctx.send(embed=emb)

    @commands.command()
    async def highfive(self, ctx, m: discord.Member = None):
        if m == None:
            m = ctx.author
        emb = discord.Embed(description=f"{ctx.author.mention} high fives {m.mention} ~ yoshh!", color=0x2e69f2)
        emb.set_image(url=return_gif('highfive'))
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
        emb.set_image(url=return_gif("handhold"))
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
