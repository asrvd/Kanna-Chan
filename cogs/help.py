import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, Select, SelectOption, InteractionType
import asyncio

gemb = discord.Embed(title="GAMES", color=0x2e69f2)
gemb.add_field(
    name="🤔 **AKINATOR**",
    value="`kana help akinator`",
    inline=True
)
gemb.add_field(
    name="🌚 **TRUTH OR DARE**",
    value="`kana help tod`",
    inline=True
)
gemb.add_field(
    name="🎰 **LOTTERY**",
    value="`kana help lotto`",
    inline=True
)
gemb.add_field(
    name="📄 **DEFINE**",
    value="`kana help def`",
    inline=True
)
gemb.add_field(
    name="❤ **MARRY**",
    value="`kana help marry`",
    inline=True
)
gemb.add_field(
    name="🥰 **SHIP**",
    value="`kana help ship`",
    inline=True
)

avemb = discord.Embed(title="🎴 **AVATAR**", description="**Command: `av`, `avatar`, `pfp`\n`kana av @user` Sends avatar of mentioned person. If no one is mentioned kanna sends your avatar.\n`kana av @user1 @user2` Sends the merged pfp of two users (matching pfp uwu).", color=0x2e69f2)

genemb = discord.Embed(title="HELP HAS COME!!", description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",color=0x2e69f2)

genemb.add_field(
    name="🔑 **PREFIX**", 
    value=f"Send `kana prefix`", 
    inline=True
)
genemb.add_field(
    name="⚙ **SOURCE**",
    value=f"Send `kana source`",
    inline=True
)
genemb.add_field(
    name="🎐 **INVITE ME**",
    value=f"[Click here](https://discord.com/api/oauth2/authorize?client_id=857835279259664403&permissions=318528&scope=bot)",
    inline=True
)
genemb.add_field(
    name="❓ **ABOUT**",
    value=f"[Click here](https://github.com/AsheeshhSenpai/Kanna-Chan/blob/main/README.md#about)",
    inline=True
)
genemb.add_field(
    name="⭐ **UPVOTE ME**",
    value=f"[Click here](https://discordbotlist.com/bots/kanna-chan/upvote)",
    inline=True
)

h = discord.Embed(
            title="ACTIONS",
            description="BOT CREATOR: [**ASHISH**](https://github.com/AsheeshhSenpai)",
            color=0x2e69f2
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


cemb = discord.Embed(title="💳 **CUSTOM CARDS**", description="`simpcard (person you simp for)` Kana makes a simpcard for you with your name and pfp on it.\n`gaycard` Kana makes a gaycard for you with your name and pfp.\n`uwucard` (mention someone) Kana makes a card to show your love for another person uwu.", color=0x2e69f2)

utilemb = discord.Embed(title="📘 **UTILITY**", color=0x2e69f2)
utilemb.add_field(
    name="👋 WELCOME MESSAGE",
    value="`kana wsetup #channel` Setup a channel where kanna will welcome users with a cute message.\n**It's an Admin/Mod only command**"
)

respemb = discord.Embed(title="**RESPONSES**", color=0x2e69f2)
respemb.add_field(
    name="😍 SIMP",
    value="`kana simp @user` Kanna sends a pickup line for the mentioned person with a cute gif uwu.",
    inline=True
)
respemb.add_field(
    name="😈 ROAST",
    value="`kana roast @user` Roast anyone *evil smile*.",
    inline=True
)

imemb = discord.Embed(title="IMAGE COMMANDS", description="**Avaialable commands**\n🐶 `woof` Sends a random doogo image.\n🐱 `meow` Sends a random catto image.", color=0x2e69f2)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def help(self, ctx, *, topic=None):
        kana = self.client.get_user(self.kana_id)
        if topic == None:
            try:
                msg=await ctx.send(embed=genemb,
                    components=[
                        Select(placeholder="Select", options=[
                        SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890"), default=True),
                        SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                        SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                        SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                        SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                        SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                        SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                        SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))]
                        )
                    ]
                )
                try:
                    while True:
                        interaction = await self.client.wait_for("select_option",timeout=40)
                        response = interaction.component[0].label
                        if response.lower() == "general":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=genemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890"), default=True),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "games":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=gemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292"), default=True), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "avatar":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=avemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363"), default=True),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "actions":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=h, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"), default=True),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "utility":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=utilemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522"), default=True),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "cards":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=cemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984"), deafult=True),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "responses":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=respemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071"), default=True),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))])])
                        elif response.lower() == "image":
                            await interaction.respond(type=InteractionType.UpdateMessage, embed=imemb, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292")), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"), deafult = True)])])
                except asyncio.TimeoutError:
                    await interaction.respond(type=InteractionType.UpdateMessage, components=[
                            Select(placeholder="Select", options=[
                            SelectOption(label="General", value="general", emoji=discord.PartialEmoji(name="kannawhat", id="721404617690316890")),
                            SelectOption(label="Games", value="games", emoji=discord.PartialEmoji(name="kannaO", id="873191889560543292"), default=True), 
                            SelectOption(label="Avatar", value="avatar", emoji=discord.PartialEmoji(name="kanna_bored", id="865149005347684363")),
                            SelectOption(label="Actions", value="actions", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654")),
                            SelectOption(label="Utility", value="utility", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                            SelectOption(label="Cards", value="cards",emoji=discord.PartialEmoji(name="ASKannaStare", id="292359094759849984")),
                            SelectOption(label="Responses", value="responses" , emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                            SelectOption(label="Image", value="image", emoji=discord.PartialEmoji(name="kannazoom", id="841107540166180915"))], disabled = True)])            
                
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
            emb = discord.Embed(title="SHIP", description="Ship two people, cus why not?\nCommand: `kanna ship`", color=0x2e69f2)
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

 
def setup(client):
    client.add_cog(Help(client))
    print(">> Help loaded")
