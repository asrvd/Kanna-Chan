import discord
from discord.ext import commands
import json
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle
import datetime
from disputils import BotConfirmation

guild_id = 864220272444571658
ccid = 879271125228593152
caid = 879270880553865246

class Confession(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def confess(self, ctx, *, desc):
        if ctx.channel.type is discord.ChannelType.private:
            kana = self.client.get_user(self.kana_id)
            await ctx.reply("Your confession has been sent! Please wait for any staff to approve it.")
            emb = discord.Embed(title="ANIMEHUB CONFESSIONS", description=f"```{desc}```", color=0xfc80e0)
            emb.timestamp = datetime.datetime.utcnow()
            emb.set_footer(
                text="DM me kana confess (your message) to confess",
                icon_url=kana.avatar_url
            )
            ca = self.client.get_channel(caid)
            cc = self.client.get_channel(ccid)

            msg1 = await ca.send(content="Send **y** to approve or **n** to disapprove.", embed=emb)
            def check(msg):
                return msg.channel.id == caid
            resp = await self.client.wait_for("message", check=check)

            if resp.content.lower() == "y":
                await cc.send(embed=emb)
                await msg1.edit(content="Approved!", embed=emb)
            elif resp.content.lower() == "n":
                await msg1.edit(content="Disapproved!", embed=emb)

        else:
            await ctx.reply("Confessions can be sent only through DM.")

def setup(client):
    client.add_cog(Confession(client))
    print(">> Confession loaded")
        
        
