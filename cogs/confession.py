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

            await ca.send(embed=emb,
                components=[
                    [
                    Button(style=ButtonStyle.green, label="Approve"),
                    Button(style=ButtonStyle.red, label="Disapprove")
                    ],
                ],
            )
            resp = await self.client.wait_for("button_click", check=None, timeout=None)
            if resp.component.label.lower() == "approve":
                await cc.send(embed=emb)
                await resp.respond(type=7, content="**Approved!**", embed=emb,
                    components=[
                    [
                    Button(style=ButtonStyle.green, label="Approve", disabled=True),
                    Button(style=ButtonStyle.red, label="Disapprove", disabled=True)
                    ],
                ],
                )
            elif resp.component.label.lower() == "disapprove":
                await resp.respond(type=7, content="**Disapproved!**", embed=emb,
                    components=[
                    [
                    Button(style=ButtonStyle.green, label="Approve", disabled=True),
                    Button(style=ButtonStyle.red, label="Disapprove", disabled=True)
                    ],
                ],
                )
            

        else:
            await ctx.reply("Confessions can be sent only through DM.")

def setup(client):
    client.add_cog(Confession(client))
    print(">> Confession loaded")
        
        
