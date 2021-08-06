import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def help(self, ctx, *, topic=None):
        kana = self.client.get_user(self.kana_id)
        if topic == None:
            try:
                h = discord.Embed(
                title="HELP HAS COME!",
                description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
                color=0x2e69f2,
                )
                h.add_field(
                name="🔑 **PREFIX**", 
                value=f"Send `kana prefix`", 
                inline=True
                )
                h.add_field(
                name="📃 **COMMANDS**",
                value=f"Send `kana cmds`",
                inline=True
                )
                h.add_field(
                name="⚙ **SOURCE**",
                value=f"Send `kana source`",
                inline=True
                )
                h.add_field(
                name="🎐 **INVITE ME**",
                value=f"[Click here](https://discord.com/api/oauth2/authorize?client_id=857835279259664403&permissions=318528&scope=bot)",
                inline=True
                )
                h.add_field(
                name="❓ **ABOUT**",
                value=f"[Click here](https://github.com/AsheeshhSenpai/Kanna-Chan/blob/main/README.md#about)",
                inline=True
                )
                h.add_field(
                name="⭐ **UPVOTE ME**",
                value=f"[Click here](https://discordbotlist.com/bots/kanna-chan/upvote)",
                inline=True
                )
                h.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
                )
                await ctx.send(embed=h)
            except Exception as e:
                print(e)
        elif topic.lower() == "akinator":
            emb = discord.Embed(title="AKINATOR", description="Start a game of Akinator using Kanna Chan!\nSend `kana akinator` to start the game. **The game is played in your DM**. To stop the game while playing send `stop` and to return to previous question send `back`.\nAll questions should be answered in `yes/no` or `y/n`.\n**Powered by: **[Akinator](https://akinator.com)", color=0x2e69f2)
            emb.set_image(url="https://static.freemake.com/blog/wp-content/uploads/2014/09/akinator-game.jpg")
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "tod":
            emb = discord.Embed(title="TRUTH OR DARE", description="Start a game of truth or dare using Kanna Chan!\nFor truth send `kanna truth` and for dare send `kanna dare`.", color=0x2e69f2)
            emb.set_image(url="https://is1-ssl.mzstatic.com/image/thumb/Purple125/v4/af/71/bc/af71bca4-9c75-2ae3-5dca-490286d51284/AppIcon-0-0-1x_U007emarketing-0-0-0-7-0-0-sRGB-0-0-0-GLES2_U002c0-512MB-85-220-0-0.jpeg/1200x630wa.png")
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "lotto":
            emb = discord.Embed(title="LOTTERY", description="Start a game of lattery using Kanna.\nYou will have to send three random numbers between 0 to 5 with space in between like `kanna lottery 1 3 4`.", color=0x2e69f2)
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "image":
            emb = discord.Embed(title="IMAGE COMMANDS", description="**Avaialable commands**\n`woof` Sends a random doogo image.\n`meow` Sends a random catto image.", color=0x2e69f2)
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "def":
            emb = discord.Embed(title="DEFINE", description="`kana df (your query here)` Kana sends the definition of your query\n**Powered by: UrbanUp**.", color=0x2e69f2)
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "marry":
            emb = discord.Embed(title="MARRY", description="Marry any person. Send `kana marry` to know more. To divorce send `kana divorce @user`", color=0x2e69f2)
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif topic.lower() == "ship":
            emb = discord.Embed(title="TRUTH OR DARE", description="Ship two people, cus why not?\nCommand: `kanna ship`", color=0x2e69f2)
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        else:
            await ctx.send("Kanna was not able to find help for this command..does this even exist?")
        

    @commands.command()
    async def source(self, ctx):
        await ctx.send("https://github.com/AsheeshhSenpai/Kanna-Chan")
        
    @commands.command()
    async def vote(self, ctx):
        emb = discord.Embed(title="UPVOTE KANNA CHAN!!", description="Vote for Kanna uwu\n[Click here](https://discordbotlist.com/bots/kanna-chan/upvote)", color=0x2e69f2)
        kana = self.client.get_user(self.kana_id)
        emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def invite(self, ctx):
        emb = discord.Embed(title="INVITE KANNA CHAN!!", description="Invite Kanna in your server uwu\n[Click here](https://discord.com/api/oauth2/authorize?client_id=857835279259664403&permissions=318528&scope=bot)", color=0x2e69f2)
        kana = self.client.get_user(self.kana_id)
        emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=emb)

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send("Prefixes for kanna are `k.`, `kana ` and `kanna `.")

    @commands.command()
    async def cmds(self, ctx):
        kana = self.client.get_user(self.kana_id)
        try:
            h = discord.Embed(
            title="COMMANDS",
            description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
            color=0x2e69f2,
            )
            h.add_field(
            name="🤪 **FUN**", 
            value=f"Send `kana fun` to see list of commands available.", 
            inline=False
            )
            h.add_field(
            name="💳 **CUSTOM CARDS**",
            value=f"`simpcard (person you simp for)` Kana makes a simpcard for you with your name and pfp on it.\n`gaycard` Kana makes a gaycard for you with your name and pfp.\n`uwucard` (mention someone) Kana makes a card to show your love for another person uwu.",
            inline=False
            )
            h.add_field(
            name="🎴 **AVATAR**",
            value=f"`av`, `avatar` or `pfp` Kana sends pfp of a user or shared pfp.",
            inline=False
            )
            h.add_field(
            name="🧩 **GAMES**",
            value=f"Send `kana games` to see list of games available and how to play them.",
            inline=False
            )
            h.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=h)
        except Exception as e:
            print(e)

    @commands.command()
    async def fun(self, ctx):
        kana = self.client.get_user(self.kana_id)
        try:
            h = discord.Embed(
            title="FUN COMMANDS",
            description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
            color=0x2e69f2,
            )
            h.add_field(
            name="❤ **Love**", 
            value=f"Kanna sends love to the person.", 
            inline=True
            )
            h.add_field(
            name="🤚 **Pat**",
            value=f"pat any person.",
            inline=True
            )
            h.add_field(
            name="🙇‍♀️ **Thank**",
            value=f"Kanna thanks the person.",
            inline=True
            )
            h.add_field(
            name="🤔 **Think**",
            value=f"Kanna thinks hmmm..",
            inline=True
            )
            h.add_field(
            name="😮 **Amazed**",
            value=f"Kanna is amazed woah..",
            inline=True
            )
            h.add_field(
            name="🫂 **Hug**",
            value=f"Kanna hugs the person.",
            inline=True
            )
            h.add_field(
            name="💃 **Dance**",
            value=f"Kanna dances with the person.",
            inline=True
            )
            h.add_field(
            name="🔪 **Kill**",
            value=f"Kanna kills the person.",
            inline=True
            )
            h.add_field(
            name="🤝 **Befriend**",
            value=f"Kanna befriends the person.",
            inline=True
            )
            h.add_field(
            name="👅 **Lick**",
            value=f"lickie lickie..",
            inline=True
            )
            h.add_field(
            name="😈 **Attack**",
            value=f"Kanna attacks",
            inline=True
            )
            h.add_field(
            name="🗣 **Say**",
            value=f"Kanna says what you want her to say.",
            inline=True
            )
            h.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=h)
        except Exception as e:
            print(e)

    @commands.command()
    async def games(self, ctx):
        kana = self.client.get_user(self.kana_id)
        emb = discord.Embed(title="GAMES", color=0x2e69f2)
        emb.add_field(
            name="🤔 **AKINATOR**",
            value="`kana help akinator`",
            inline=True
        )
        emb.add_field(
            name="🌚 **TRUTH OR DARE**",
            value="`kana help tod`",
            inline=True
        )
        emb.add_field(
            name="🎰 **LOTTERY**",
            value="`kana help lotto`",
            inline=True
        )
        emb.add_field(
            name="📄 **DEFINE**",
            value="`kana help def`",
            inline=True
        )
        emb.add_field(
            name="❤ **MARRY**",
            value="`kana help marry`",
            inline=True
        )
        emb.add_field(
            name="🥰 **SHIP**",
            value="`kana help ship`",
            inline=True
        )
        emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=emb)

def setup(client):
    client.add_cog(Help(client))
    print(">> Help loaded")
