import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import pyrebase
import json
from decouple import config
from disputils import BotEmbedPaginator
from PIL import Image, ImageDraw, ImageFont

firebase = pyrebase.initialize_app(json.loads(config("firebaseConfig")))
db = firebase.database()

def create(guild, channel):    #stores guild ID and channel ID
    db.child("WELCOME").child(guild).set({"CHANNEL": channel})

def return_channel(guild):     #returns channel ID
    channel = db.child("WELCOME").child(guild).child("CHANNEL").get().val()
    if channel == None:
        return None
    else:
        return channel

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def wsetup(self, ctx, *, channel: discord.TextChannel = None):
        create(ctx.guild.id, channel.id)
        await ctx.send(f">> Welcome messages have been setup to {channel.mention} now.")
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = return_channel(member.guild.id)
        channel = self.client.get_channel(channel_id)
        if channel_id == None:
            return
        elif channel_id != None:
            guild_name = member.guild.name
            name = member.name
            id = member.discriminator
            f1 = ImageFont.truetype('./fonts/Magz.otf', 128)
            f2 = ImageFont.truetype('./fonts/Magz.otf', 64)
            desc = f"Welcome {member.mention} to the Server **{guild_name}**!"
            bg = Image.new('RGBA', (1000, 200), (255, 0, 0, 0))
            asset = member.avatar_url_as(format='png', size=256)
            await asset.save('av.png')
            im = Image.open('av.png')
            im = im.resize((200, 200))
            mask = Image.new('L', (200, 200), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse((0, 0, 200, 200), fill=255)
            mask.save('mask.jpg')
            bg.paste(im, (30, 0), mask)
            draw = ImageDraw.Draw(bg)
            draw.text((300, 20), name, (144, 66, 245), font=f1)
            draw.text((300, 119), id, (247, 87, 237), font=f2)
            bg.save('final.png')
            file = discord.File('final.png')
            await channel.send(desc, file=file)


    @commands.command()
    async def enlarge(self, ctx, *, content):
        cont = content.split()
        embeds = []
        for word in cont:
            if word.startswith("<") and word.endswith(">"):
                lst = word.strip("<:a>").split(":")
                if word.startswith("<a:"):
                    emoj = discord.PartialEmoji(name=lst[0], id=lst[1], animated=True)
                else:
                    emoj = discord.PartialEmoji(name=lst[0], id=lst[1])
                asset = emoj.url
                emb = discord.Embed(description=f"`{lst[1]}`\n`{lst[0]}`", color=0x2e69f2)
                emb.set_image(url=str(asset))
                embeds.append(emb)
        paginator = BotEmbedPaginator(ctx, embeds, control_emojis=("⏮", "◀", "▶", "⏭"))
        await paginator.run()

def setup(client):
  client.add_cog(Utility(client))
  print(">> Utility loaded")
