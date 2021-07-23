import discord
from discord.ext import commands
from PIL import Image, ImageDraw
from io import BytesIO

class Roleplay(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def dance(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"kanna dances with {ctx.author.mention} uwu", color=0x2e69f2)
        emb.set_image(url="https://gifimage.net/wp-content/uploads/2018/04/kanna-gif-8.gif")
        await ctx.send(embed=emb)
 
    @commands.command()
    async def hug(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"Kanna hugs {mem.mention} uwu", color=0x2e69f2)
        emb.set_image(url="https://giffiles.alphacoders.com/187/187466.gif")
        await ctx.send(embed=emb)

    @commands.command()
    async def kill(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"{ctx.author.mention} kills {mem.mention}", color=0x2e69f2)
        emb.set_image(url="https://media1.tenor.com/images/28c19622e8d7362ccc140bb24e4089ec/tenor.gif")
        await ctx.send(embed=emb)

    @commands.command()
    async def attack(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"{mem.mention} Behold the power of Dragon Loli!", color=0x2e69f2)
        emb.set_image(url="https://i.pinimg.com/originals/5d/db/a3/5ddba3cec2b283d94b66abd7314b6cbd.gif")
        await ctx.send(embed=emb)

    @commands.command()
    async def lick(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"{ctx.author.mention} licks {mem.mention}, tastes good :)", color=0x2e69f2)
        emb.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/001/230/497/04d.gif")
        await ctx.send(embed=emb)

    @commands.command()
    async def think(ctx):
        emb = discord.Embed(title="", description=f"Kanna thinks hmmm..", color=0x2e69f2)
        emb.set_image(url="https://i.pinimg.com/originals/4f/b6/4c/4fb64c59ff0394033f61b6c018d61ed1.gif")
        await ctx.send(embed=emb)
  
    @commands.command()
    async def amazed(ctx):
        emb = discord.Embed(title="", description=f"Kanna is amazed woah..", color=0x2e69f2)
        emb.set_image(url="https://preview.redd.it/n5ptq0iw65351.png?width=640&crop=smart&auto=webp&s=75887b8b7e949f52c4f548dd5d037249dca05566")
        await ctx.send(embed=emb)

    @commands.command()
    async def pat(ctx, m1: discord.Member = None, m2: discord.Member = None):
        if m1 == None:
            m1 = ctx.author
            m2 = ctx.author
        elif m2 == None:
            m2 = m1
            m1 = ctx.author
        size = (128, 128)
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + size, fill=255)
        bg = Image.open("./images/kanna_pat.png")
        asset1 = m1.avatar_url_as(size=256)
        asset2 = m2.avatar_url_as(size=256)
        data1 = BytesIO(await asset1.read())
        data2 = BytesIO(await asset2.read())
        pfp1 = Image.open(data1).convert('RGBA')
        pfp2 = Image.open(data2).convert('RGBA')
        pfp1 = pfp1.resize((122, 122))
        pfp2 = pfp2.resize((122, 122))
        pfp1.save('pfp1.png')
        pfp2.save('pfp2.png')

        bg.paste(pfp1, (122, 86))
        bg.paste(pfp2, (355, 82))

        bg.save("avatar.png")
        file = discord.File("avatar.png")
        emb = discord.Embed(title="", description=f"{m1.mention} pats {m2.mention} uwu", color=0x2e69f2)
        emb.set_image(url="attachment://avatar.png")
        await ctx.send(embed=emb, file=file)
    
    @commands.command()
    async def love(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"Kanna sends love to {mem.mention} uwu", color=0x2e69f2)
        emb.set_image(url="https://pa1.narvii.com/7231/f52073bab90f9a13f3e292af0b3e1b1e8f8ba189r1-540-304_hq.gif")
        await ctx.send(embed=emb)

    @commands.command()
    async def thank(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author.id
        emb = discord.Embed(title="", description=f"Arigatou {mem.mention} :)", color=0x2e69f2)
        emb.set_image(url="https://i.ytimg.com/vi/ALEFgAbDE8U/maxresdefault.jpg")
        await ctx.send(embed=emb)

    @commands.command()
    async def befriend(ctx, mem: discord.User = None):
        if mem == None:
            mem = ctx.author
        emb = discord.Embed(title="", description=f"Kanna is your friend now uwu {mem.mention} :)", color=0x2e69f2)
        emb.set_image(url="https://i.pinimg.com/originals/d9/ff/de/d9ffde3f3d3114ca7012f6c6c153ec55.jpg")
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Roleplay(client))
    print(">> Roleplay loaded")