import discord
from discord.ext import commands
import random
import json
import requests
from discord import utils
from decouple import config
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle, InteractionType
import asyncio

rapid_api = str(config("RAPID_API_KEY"))
word_api = str(config("WORD_API_KEY"))

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def truth(self, ctx):
        truth = [
        "When was the last time you lied?",
        "When was the last time you cried?",
        "What's your biggest fear?",
        "What's your biggest fantasy?",
        "Do you have any fetishes?",
        "What's something you're glad your mum doesn't know about you?",
        "Have you ever cheated on someone?",
        "What's the worst thing you've ever done?",
        "What's a secret you've never told anyone?",
        "Do you have a hidden talent?",
        "Who was your first celebrity crush?",
        "What are your thoughts on politicians?",
        "What's the worst intimate experience you've ever had?",
        "Have you ever cheated in an exam?",
        "What's the most drunk you've ever been?",
        "Have you ever broken the law?",
        "What's the most embarrassing thing you've ever done?",
        "What's your biggest insecurity?",
        "What's the biggest mistake you've ever made?",
        "What's the most disgusting thing you've ever done?",
        "Who would you like to kiss in this server?",
        "What's the worst thing anyone's ever done to you?",
        "Have you ever had a run in with the law?",
        "What's your worst habit?",
        "What's the worst thing you've ever said to anyone?",
        "Have you ever peed in the shower?",
        "What's the strangest dream you've had?",
        "Have you ever been caught doing something you shouldn't have?",
        "What's the worst date you've been on?",
        "What's your biggest regret?",
        "What's the biggest misconception about you?",
        "Are you virgin?",
        "Why did your last relationship break down?",
        "Have you ever lied to get out of a bad date?",
        "What's the most trouble you've been in?"
        ]
        await ctx.send(f"Truth: {random.choice(truth)}")

    @commands.command()
    async def dare(self, ctx):
        dare = [
        "Show the most embarrassing photo on your phone",
        "Show the last five people you texted and what the messages said",
        "Let the rest of the group DM someone from your Instagram account",
        "Eat a raw piece of garlic",
        "Do 100 squats",
        "Keep three ice cubes in your mouth until they melt",
        "Say something dirty to the person on your left",
        "Give a foot massage to the person on your right",
        "Put 10 different available liquids into a cup and drink it",
        "Yell out the first word that comes to your mind",
        "Give a lap dance to someone of your choice",
        "Remove four items of clothing",
        "Like the first 15 posts on your Facebook newsfeed",
        "Eat a spoonful of mustard",
        "Keep your eyes closed until it's your go again",
        "Send a text to the last person in your phonebook",
        "Show off your orgasm face",
        "Seductively eat a banana",
        "Empty out your wallet/purse and show everyone what's inside",
        "Do your best sexy crawl",
        "Pretend to be the person to your right for 10 minutes",
        "Eat a snack without using your hands",
        "Say two honest things about everyone else in the group",
        "Twerk for a minute",
        "Try and make the group laugh as quickly as possible",
        "Try to put your whole fist in your mouth",
        "Tell everyone an embarrassing story about yourself",
        "Try to lick your elbow",
        "Post the oldest selfie on your phone on Instagram Stories",
        "Tell the saddest story you know",
        "Howl like a wolf for two minutes",
        "Dance without music for two minutes",
        "Pole dance with an imaginary pole",
        "Let someone else tickle you and try not to laugh",
        "Put as many snacks into your mouth at once as you can"
        ]
        await ctx.send(f"Dare: {random.choice(dare)}")

    @commands.command(aliases=["uns"])
    async def unscramble(self, ctx):
        kana = self.client.get_user(self.kana_id)
        url = "https://random-words5.p.rapidapi.com/getRandom"
        headers = {
            'x-rapidapi-key': word_api,
            'x-rapidapi-host': "random-words5.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers)
        word = response.text
        wlist = list(response.text)
        random.shuffle(wlist)
        sword = ''.join(wlist)
        emb = discord.Embed(title=f"{ctx.author.display_name}'s UNSCRAMBLE game!", description=f"**Unscramble the word [{sword}] and write the unscrambled word in chat.\nYou have 40s to answer!!**", color=0x2e69f2)
        emb.set_footer(
          text = "For more games send kana help",
          icon_url= kana.avatar_url 
        )
        msg = await ctx.send(embed=emb)
        wemb = discord.Embed(title=f"{ctx.author.display_name}'s UNSCRAMBLE game!", description=f"**😏 You won the game!\nThe word was {word}!!**", color=0x2e69f2)
        wemb.set_footer(
          text = "For more games send kana help",
          icon_url= kana.avatar_url 
        )
        lemb = discord.Embed(title=f"{ctx.author.display_name}'s UNSCRAMBLE game!", description=f"**😞 You lost the game..\nThe word was {word}. Better luck next time.**", color=0x2e69f2)
        lemb.set_footer(
          text = "For more games send kana help",
          icon_url= kana.avatar_url 
        )
        try:
            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel
            response = await self.client.wait_for('message', check=check, timeout=40)
            if response.content.lower() == word:
                await msg.edit(embed=wemb)
            elif response.content.lower() != word:
                await msg.edit(embed=lemb)
        except asyncio.TimeoutError:
            await msg.edit(embed=lemb, content=f"{ctx.author.mention}\n😞 You took too long to answer, You lost the game.")

    @commands.command(aliases=['lotto'])
    async def lottery(self, ctx, *, guesses):
        #Enter the lottery and see if you win!
        numbers = []
        for x in range(3):
            numbers.append(random.randint(0, 9))

        split = guesses.split(' ')
        if len(split) != 3:
            return await ctx.send('Please separate your numbers with a space, and make sure there are 3 numbers between 0 and 9.')
        string_numbers = [str(i) for i in numbers]
        if split[0] == string_numbers[0] and split[1] == string_numbers[1] and split[2] == string_numbers[2]:
            await ctx.send(f'{ctx.author.mention} You won! Congratulations on winning the lottery!')
        else:
            await ctx.send(f"{ctx.author.mention} Better luck next time... You were one of the 124/125 who lost the lottery...\nThe numbers were `{', '.join(string_numbers)}`")

    @commands.command()
    async def rps(self, ctx):
        def return_embed(kana, user):
            cond = ""
            if kana == user:
                cond = "t"
            game = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
            if game[user] == kana:
                cond = "w"
            elif game[user] != kana and kana != user:
                cond = "l"
            if cond == "t":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description="**🙂 Oops, It's a draw..\nTry again :)**", color=0x2e69f2)
                return emb
            elif cond == "w":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description=f"**😏 You won the game!\nI chose {kana} and you chose {user}!**", color=0x2e69f2)
                return emb
            elif cond == "l":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description=f"**😞 You lost the game, Better luck next time..\nI chose {kana} and you chose {user}.**", color=0x2e69f2)
                return emb


        emb = discord.Embed(title=f"{ctx.author.display_name}'s RPS game!", description="**rock, paper, scissors..\nClick on any one button to play the game!**", color=0x2e69f2)
        msg=await ctx.send(embed=emb,
            components=[
                [
                Button(style=ButtonStyle.blue, label="Rock", emoji="✊"),
                Button(style=ButtonStyle.red, label="Paper", emoji="🤚"),
                Button(style=ButtonStyle.green, label="Scissors", emoji="✌")
                ],
            ],
        )
        try:
            def check(resp):
                return resp.user == ctx.author and resp.channel == ctx.channel
        
            resp = await self.client.wait_for("button_click", check=check, timeout=60)
            bot = random.choice(["rock", "paper", "scissors"])
            player = resp.component.label.lower()
            embed = return_embed(bot, player)
            await resp.respond(type=InteractionType.UpdateMessage, embed=embed,
                components=[
                    [
                    Button(style=ButtonStyle.blue, label="Rock", emoji="✊", disabled=True),
                    Button(style=ButtonStyle.red, label="Paper", emoji="🤚", disabled=True),
                    Button(style=ButtonStyle.green, label="Scissors", emoji="✌", disabled=True)
                    ],
                ],
            ) 
        except asyncio.TimeoutError:
            await msg.edit(components=[[
                Button(style=ButtonStyle.blue, label="Rock", emoji="✊", disabled=True),
                Button(style=ButtonStyle.red, label="Paper", emoji="🤚", disabled=True),
                Button(style=ButtonStyle.green, label="Scissors", emoji="✌", disabled=True),
                ],],)

    @commands.command(aliases=['hl'])
    async def highlow(self, ctx,):
        def return_embed(num1, num2, guess):
            cond = ""
            if num1 == num2:
                cond = "t"
            elif num1 > num2 and guess == "high":
                cond = "w"
            elif num1 < num2 and guess == "low":
                cond = "w"
            else:
                cond = "l"
            if cond == "t":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**😏 woah, It's a JACKPOT!!\nThe number was exactly {num2}!**", color=0x2e69f2)
                return emb
            elif cond == "w":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**🙂 You won the game!\nThe number was {num1}!**", color=0x2e69f2)
                return emb
            elif cond == "l":
                emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**😞 You lost the game, Better luck next time..\nThe number was {num1}.**", color=0x2e69f2)
                return emb
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        emb = discord.Embed(title=f"{ctx.author.display_name}'s HIGHLOW game!", description=f"**Guess whether the number is higher or lower than {n2}.\nYou have 30s to answer!**", color=0x2e69f2)
        msg=await ctx.send(embed=emb,
            components=[
                [
                Button(style=ButtonStyle.blue, label="HIGH", emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071")),
                Button(style=ButtonStyle.blue, label="JACKPOT!", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522")),
                Button(style=ButtonStyle.blue, label="LOW", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"))
                ],
            ],
        )
        try:
            def check(resp):
                return resp.user == ctx.author and resp.channel == ctx.channel
        
            resp = await self.client.wait_for("button_click", check=check, timeout=30)
            player = resp.component.label.lower()
            embed = return_embed(n1, n2, player)
            await resp.respond(type=InteractionType.UpdateMessage, embed=embed,
                components=[
                    [
                    Button(style=ButtonStyle.blue, label="HIGH", emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071"), disabled=True),
                    Button(style=ButtonStyle.blue, label="JACKPOT!", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522"), disabled=True),
                    Button(style=ButtonStyle.blue, label="LOW", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"), disabled=True)
                    ],
                ],
            ) 
        except asyncio.TimeoutError:
            await msg.edit(components=[[
                Button(style=ButtonStyle.blue, label="HIGH", emoji=discord.PartialEmoji(name="KannaAwh", id="758724574010409071"), disabled=True),
                Button(style=ButtonStyle.blue, label="JACKPOT!", emoji=discord.PartialEmoji(name="RWKannaSmug", id="762995028200128522"), disabled=True),
                Button(style=ButtonStyle.blue, label="LOW", emoji=discord.PartialEmoji(name="kannah", id="873191866387013654"), disabled=True)
                ],],)

    @commands.command(aliases=["df"])
    async def define(self, ctx, *, query):
        kana = self.client.get_user(self.kana_id)
        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term":f"{query}"}
        headers = {
            'x-rapidapi-key': rapid_api,
            'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com"
        }
        res = requests.request("GET", url, headers=headers, params=querystring)
        result = res.content
        json_data = json.loads(result)
        list = json_data["list"]
        if list == []:
            await ctx.send("No results available for this query ;-;")
        else:
            jtext = json_data["list"][0]["definition"]
            example = json_data["list"][0]["example"]
            link = json_data["list"][0]["permalink"]
            emb = discord.Embed(description=f"{jtext}\n\n*`{example}`*\n\n*more results at {link}*", color=0x2e69f2)
            emb.set_author(name=f"Definition Of {query.capitalize()}", icon_url=ctx.author.avatar_url)
            emb.set_footer(text="Kanna Chan", icon_url=kana.avatar_url)
            await ctx.send(embed=emb)

    @commands.command()
    async def ship(self, ctx, m1: discord.User = None, m2: discord.User = None):
        if m1 == None:
            m1 = ctx.author
            m2 = ctx.author
        elif m2 == None:
            m2 = m1
            m1 = ctx.author

        ship_list=[
            "Possible..",
            "Not in this life..",
            "Maybe..",
            "Best couple!",
            "Looks impossible..",
            "Fated partners..",
            "Should already be in this relationship.."
        ]

        await ctx.send(f"{m1.mention} X {m2.mention}\n{random.choice(ship_list)}")

    @commands.command()
    async def bot(self, ctx, *, message):
        webhooks = await ctx.channel.webhooks()
        webhook = utils.get(webhooks, name="Kanna")
        if webhook is None:
            webhook = await ctx.channel.create_webhook(name = "Kanna")
        await webhook.send(message, username = ctx.author.name, avatar_url = ctx.author.avatar_url)
        await ctx.message.delete()

def setup(client):
    client.add_cog(Games(client))
    print(">> Games loaded")
