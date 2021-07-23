import discord
from discord.ext import commands
import random

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def arz(self, ctx):
        shayari=[
            "*samundar ke kinare abadi nahi hoti, jisse pyar ho usse shadi nhi hoti..\n~SENSEI*",
            "*Ladki ka hasna adda hai, jo use pyaar samjhe vo gadha hai..\n~SENSEI*",
            "*tera bhi katega..\n~SENSEI*",
            "*kadu kata hai mere dost intejaar kar sabme batega,\nishq hua hai? intejaar kar tera bhi katega..\n~SENSEI*",
            "*ab na tere aana ki khushi rhi na tere jaane ka gam,\nvo jamana beet gya jab tere diwane the hum..\n~SENSEI*",
            "*Wo tumhen DP dikhaakar gumraah karegi,\nMagar Tum Aadhaar card par adde rehna..\n~KAKASHI*",
            "*yeh waqt bhi guzar jayega..\n~KAKASHI*",
            "*na reply chahiye\nna tera sath\nnikal meri zindagi se\nnahi karni tujhse koi baat..\n~SENSEI*",
            "*insaan ka dil bara hona chaiye, chota to mera dongle bhi he..\n~SAIYAN*",
            "*age is just a number, jail is just a room..\n~DA 8 YEAR OLD*"
            ]
        emb = discord.Embed(title="arz kiya hai..", description=f"{random.choice(shayari)}", color=0x2e69f2)
        await ctx.send(embed=emb)

    @commands.command()
    async def say(self, ctx, *, message):
        emb = discord.Embed(title=message, description=f"by {ctx.author.mention}", color=0x2e69f2)
        await ctx.send(embed=emb)

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.client.process_commands(message)

        love_words=[
            "i love you kanna chan",
            "love you kanna chan",
            "kanna chan i love you",
            "i love kanna chan",
            "kanna chan is love",
            "i love you kanna",
            "love you kanna"
        ]

        hate_words=[
            "i hate you kanna chan",
            "hate you kanna chan",
            "kanna chan i hate you",
            "kanna chan hate",
            "i hate you kanna",
            "hate you kanna"
        ]

        love_emb = discord.Embed(title="", description=f"Kanna loves you too {message.author.mention} uwu", color=0x2e69f2)
        love_emb.set_image(url="https://pa1.narvii.com/7231/f52073bab90f9a13f3e292af0b3e1b1e8f8ba189r1-540-304_hq.gif")
        
        hate_emb = discord.Embed(title="", description=f"Kanna is sad :( {message.author.mention} Kanna loves you :(", color=0x2e69f2)
        hate_emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/349/853/60b.gif")

        if message.content.lower() in love_words:
            if message.author.id == 784363251940458516:
                await message.channel.send(f"{message.author.mention}\nKanna loves asheesh too uwu..❤")
                await message.add_reaction('❤')
            else: 
                await message.channel.send(embed=love_emb)
                await message.add_reaction('❤')
        elif message.content.lower() in hate_words:
            if message.author.id == 784363251940458516:
                await message.channel.send(f"{message.author.mention}\nBut Kanna loves asheesh..❤")
                await message.add_reaction('❤')
            else: 
                await message.channel.send(embed=hate_emb)
                await message.add_reaction('❤')

def setup(client):
    client.add_cog(Misc(client))
    print(">> Misc loaded")