import discord
from discord.ext import commands
import pyrebase
import json
from decouple import config
from disputils import BotEmbedPaginator

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
    @commands.is_owner()
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
            desc = f"Everyone, welcome our newest member {member.mention}!"
            file = discord.File("./images/welcome.gif")
            embed = discord.Embed(title="NEW MEMBER!", description=desc, color=0x2e69f2)
            embed.set_image(url="attachment://welcome.gif")
            await channel.send(member.mention, embed=embed, file=file)

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
