import discord
from discord.ext import commands
import pyrebase
import json
from decouple import config

firebase = pyrebase.initialize_app(json.loads(config("firebaseConfig")))
db = firebase.database()

def create(guild, channel):    #stores marriage info in database
    db.child("WELCOME").child(guild).set({"CHANNEL": channel})

def return_channel(guild):
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

def setup(client):
  client.add_cog(Utility(client))
  print(">> Utility loaded")
