import discord
from discord.ext import commands

arrow = "<a:righter_arrow:509735362994896924>"
kwee = "<:kannawee:877036162122924072>"
kdance = "<a:kanna_dance:877038778798207016>"
kbored = "<:kanna_bored:877036162827583538>"
ksmug = "<:kanna_smug:877038777896427560>"
heart = "<a:WhiteHeartExplosion:821865122443296768>"

class Server(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    @commands.is_owner()
    async def sabout(self, ctx):
        kana = self.client.get_user(self.kana_id)
        about_file = discord.File("./images/about_server.png")
        await ctx.send(file = about_file)
        emb = discord.Embed(title=f"{kdance} ABOUT SERVER {kdance}",description = f"{arrow} **DRAGON LOLI'S HOME** is the official Server of the bot **Kanna Chan**. It's a friendly community meant for having fun, chilling and spending time with others.\n{arrow} This server has cute emotes and a lot of fun events are about to be done here! So, stay tuned!", color=0xfc74c6)
        emb.add_field(
            name=f"{kwee} __ROLES__",
            value=f"{arrow} <@&876800883441156138> The highest role supposed to be only for Kanna Chan.\n{arrow} <@&876817811396263946> Admins of the Server and have the highest power and authority after owner.\n{arrow} <@&876818242058997791> Moderators of the server meant to moderate the chat and maintain a positive environment in community.\n{arrow} <@&876801038420701196> Developer(s) of Kanna Chan have this role.\n{arrow} <@&876804164661944340> All other users who join this server get this role by default. They have image and embed perms by deault.\n{arrow} **PS: APART FROM THESE SELF-ROLES ARE ALSO AVAIALBLE FOR MEMBERS.**",
            inline=False
        )
        emb.add_field(
            name=f"{ksmug} __CHANNELS__",
            value=f"{arrow} <#877030933847490691> Read the rules here.\n{arrow} <#877031867440832574> Channel for grabbing self-roles.\n{arrow} <#876798564704084011> The general chat for the server.\n{arrow} <#876798809819189249> Bot Commands should be executed here.\n{arrow} <#876798696078065694> You can give suggestions for improving Kanna Chan here.\n{arrow} <#876798720254029864> You can report BUGS here if you find any in Kanna Chan.\n{arrow} <#876798750876651530> For any other support or query use this channel.\n{arrow} **P.S: YOU CAN PING ANY STAFF MEMBER OR DEVELOPER WHILE REPORTING BUG OR IN CASE OF ANY QUERY.**",
            inline=False
        )
        emb.set_footer(
            text="Kanna Chan",
            icon_url=kana.avatar_url
        )
        await ctx.send(embed=emb)

    @commands.command()
    @commands.is_owner()
    async def rule(self, ctx):
        kana = self.client.get_user(self.kana_id)
        rule_file = discord.File("./images/rules.png")
        await ctx.send(file=rule_file)
        emb = discord.Embed(title=f"{kbored} RULES {kbored}", color=0xfc74c6)
        emb.add_field(
            name=f"{heart} **Be respectful**",
            value=f"You must respect all users, regardless of your liking towards them. Treat others the way you want to be treated.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **No Inappropriate Language**",
            value=f"{arrow} The use of profanity should be kept to a minimum. However, any derogatory language towards any user is prohibited.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **No spamming**",
            value=f"{arrow} Don't send a lot of small messages right after each other. Do not disrupt chat by spamming.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **No pornographic/adult/other NSFW material**",
            value=f"{arrow} This is a community server and not meant to share this kind of material.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **No advertisements**",
            value=f"{arrow} We do not tolerate any kind of advertisements, whether it be for other communities or streams. You can post your content in the media channel if it is relevant and provides actual value (Video/Art)",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **No offensive names and profile pictures**",
            value=f"{arrow} You will be asked to change your name or picture if the staff deems them inappropriate.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **Server Raiding**",
            value=f"{arrow} Raiding or mentions of raiding are not allowed.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **Direct & Indirect Threats**",
            value=f"{arrow} Threats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed.",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **Follow the Discord Community Guidelines**",
            value=f"{arrow} You can find them here: https://discordapp.com/guidelines",
            inline=False
        )
        emb.add_field(
            name=f"{heart} **Do not join voice chat channels without permission of the people already in there.**",
            value=f"",
            inline=False
        )
        emb.add_field(
            name=f"{heart} ***The Admins and Mods will Mute/Kick/Ban per discretion. If you feel mistreated dm an Admin and we will resolve the issue.***",
            value=f"",
            inline=False
        )
        emb.add_field(
            name=f"{heart} ***Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them.***",
            value=f"",
            inline=False
        )
        emb.set_footer(
            text="Kanna Chan",
            icon_url=kana.avatar_url
        )
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Server(client))
    print(">> Server Utility loaded")