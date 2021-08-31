import discord
from discord.ext import commands
import pyrebase
from decouple import config
import json
import datetime
from discord_components import DiscordComponents, Button, Select, SelectOption, ButtonStyle

firebase = pyrebase.initialize_app(json.loads(config("firebaseConfig")))
db = firebase.database()

def create(mem1, mem2):    #stores marriage info in database
    now = str(datetime.date.today())
    db.child("MARRIAGE").child(mem1).set({"PARTNER": mem2, "TIME": now})

def mcheck(user1, user2 = None):   
    auth1 = db.child("MARRIAGE").child(user1).get().val()
    auth2 = db.child("MARRIAGE").child(user2).get().val()
    all_users = db.child("MARRIAGE").get()
    if all_users.each() != None:
        for user in all_users.each():
            partner = db.child("MARRIAGE").child(user.key()).child("PARTNER").get().val()
            if partner == user1 or partner == user2:
                return True
                break
    if auth1 != None or auth2 != None:
        return True
    else:
        return False

def scheck(user):   #checks if user is married or not
    auth1 = db.child("MARRIAGE").child(user).get().val()
    all_users = db.child("MARRIAGE").get()
    if all_users.each() != None:
        for users in all_users.each():
            partner = db.child("MARRIAGE").child(users.key()).child("PARTNER").get().val()
            if partner == user:
                return True
                break
    if auth1 != None:
        return True
    else:
        return False

def return_partner(user):  #returns ID of partner
    auth = db.child("MARRIAGE").child(user).get().val()
    if auth == None:
        all_users = db.child("MARRIAGE").get()
        if all_users.each() != None:
            for users in all_users.each():
                partner = db.child("MARRIAGE").child(users.key()).child("PARTNER").get().val()
                if partner == user:
                    p = users.key()
                    break
    else:
        p = db.child("MARRIAGE").child(user).child("PARTNER").get().val()
    return p

def check_partner(user1, user2):   #checks if person is his/her partner
    auth1 = db.child("MARRIAGE").child(user1).child("PARTNER").get().val()
    auth2 = db.child("MARRIAGE").child(user2).child("PARTNER").get().val()
    if user1 == auth2 or user2 == auth1:
        return True
    else:
        return False

def return_time(user):   #returns date of marriage
    auth = db.child("MARRIAGE").child(user).get().val()
    if auth == None:
        all_users = db.child("MARRIAGE").get()
        if all_users.each() != None:
            for users in all_users.each():
                partner = db.child("MARRIAGE").child(users.key()).child("PARTNER").get().val()
                if partner == user:
                    user = users.key()
            time = db.child("MARRIAGE").child(user).child("TIME").get().val()
    else:
        time = db.child("MARRIAGE").child(user).child("TIME").get().val()
    return time

def remove(user1, user2):  #removes user info after divorce
    list = [user1, user2]
    for user in list:
        auth = db.child("MARRIAGE").child(user).get().val()
        if auth != None:
            db.child("MARRIAGE").child(user).remove()

class Marry(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def marry(self, ctx, mem: discord.User = None):
        kana = self.client.get_user(self.kana_id)
        if mem == None:
            emb=discord.Embed(description="You need to mention someone to marry them\nThe command is `marry @user`.")
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            await ctx.send(embed=emb)
        elif mem.id == ctx.author.id:
            await ctx.reply("You can't marry yourself, dumb <:dum:864375070196367400>")
        elif mem.id == self.kana_id:
            await ctx.reply("You can't marry me, I'm a minor!! Hello, FBI? <:kanna_fbi:877036161812561960>")
        elif mem.bot:
            await ctx.reply("You want to marry a bot? I understand you are not getting real girls but you gotta try <:kanna_suicide:877038776013176832>")
        else:
            if mcheck(ctx.author.id, mem.id) == False:
                author = ctx.author.name
                desc = f":ring: **{author}** has proposed to **{mem.name}** :ring:\n\n{mem.name} , Do you accept this proposal?\n**Type yes to accept or no to decline.**"
                em = discord.Embed(title="MARRIAGE PROPOSAL!", description=desc,color=0x2e69f2)
                em.set_author(
                        name="Marriage!",
                        icon_url=ctx.author.avatar_url
                )
                em.set_footer(
                text=f"Kanna Chan",
                icon_url=kana.avatar_url,
                )
                await ctx.send(mem.mention, embed=em)
                def check(m):
                    return m.author == mem
                response = await self.client.wait_for('message', check=check, timeout=40)
                if response.content.lower().strip() == "yes":
                    msg = f"<a:yayy:882300913920917514> {author} and {mem.name}\n\nYou are married now uwu <a:yayy:882300913920917514>"
                    em1 = discord.Embed(title=":heart: Congratulations!! :heart:", description=msg, color=0x2e69f2)
                    em1.set_author(
                        name="Marriage!",
                        icon_url=ctx.author.avatar_url
                    )
                    em1.set_footer(
                    text=f"Kanna Chan",
                    icon_url=kana.avatar_url,
                    )
                    em1.set_image(url="https://c.tenor.com/onRe_6jABMcAAAAC/ring-will-you-marry-me.gif")
                    await ctx.send(embed=em1)
                    create(ctx.author.id, mem.id)
                elif response.content.lower().strip() == "no":
                    msg = "The proposal between " + author + " and " + mem.name + " has been declined."
                    em2 = discord.Embed(title=f"<a:kanna_cry:877036167206420500> {ctx.author.mention} your proposal was declined <a:kanna_cry:877036167206420500>", description=msg, color=0x2e69f2)
                    em2.set_author(
                        name="Marriage!",
                        icon_url=ctx.author.avatar_url
                    )
                    em2.set_footer(
                    text=f"Kanna Chan",
                    icon_url=kana.avatar_url,
                    )
                    await ctx.send(ctx.author.mention, embed=em2)
            else:
                await ctx.reply("Anyone of you is already married ;-;")

    @commands.command()
    async def marriage(self, ctx):
        kana = self.client.get_user(self.kana_id)
        if scheck(ctx.author.id) == True:
            partner = self.client.get_user(int(return_partner(ctx.author.id)))
            partner_name = partner.name
            then = return_time(ctx.author.id)
            thatday = datetime.datetime.strptime(then ,'%Y-%m-%d')
            month = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
            emb = discord.Embed(description=f"**{ctx.author.name}** is married to **{partner_name}** uwu\n\nMarried since {thatday.day} {month[thatday.month]}, {thatday.year} <a:woww:882301342377459772>\nYou are cute <:cute_stare:882300914101289031>", color=0x2e69f2)
            emb.set_author(
                name=f"{ctx.author.name.lower()}'s Marriage Card",
                icon_url=ctx.author.avatar_url
            )
            emb.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
            )
            emb.set_image(url="https://c.tenor.com/8CZQ5N0SPKAAAAAC/mochi-cat.gif")
            await ctx.send(ctx.author.mention, embed = emb)
        else:
            await ctx.reply(f"{ctx.author.mention} You are currently not married to anyone.")

    @commands.command()
    async def divorce(self, ctx, mem: discord.User = None):
        kana = self.client.get_user(self.kana_id)
        if mem == ctx.author:
            await ctx.reply("How do you divorce with yourself baka! <:dum:864375070196367400>")
        elif mem == None:
            await ctx.reply("Mention your partner to divorce with!")
        else:
            if check_partner(ctx.author.id, mem.id) == True:
                author = ctx.author.name
                desc = f" **{author}** wants to divorce with **{mem.name}** \n\n{mem.name} , Do you accept this divorce notice?\n**Type yes to accept or no to decline.**"
                em = discord.Embed(title="✉ DIVORCE NOTICE! ✉", description=desc,color=0x2e69f2)
                em.set_footer(
                    text=f"Kanna Chan",
                    icon_url=kana.avatar_url,
                )
                await ctx.send(mem.mention, embed=em)
                def check(m):
                    return m.author == mem
                response = await self.client.wait_for('message', check=check, timeout=40)
                if response.content.lower().strip() == "yes":
                    msg = f"{author} and {mem.name} have taken divorce ;-;\n\nYou are no more married now."
                    em1 = discord.Embed(title=":broken_heart: Divorce :broken_heart:", description=msg, color=0x2e69f2)
                    em1.set_footer(
                    text=f"Kanna Chan",
                    icon_url=kana.avatar_url,
                    )
                    await ctx.send(embed=em1)
                    remove(ctx.author.id, mem.id)
                elif response.content.lower().strip() == "no":
                    msg = f"{ctx.author.mention} {mem.name} doesn't want to divorce with you ;-;.\nPlease sort out things on your own ;-;"
                    em2 = discord.Embed(description=msg, color=0x2e69f2)
                    em2.set_footer(
                    text=f"Kanna Chan",
                    icon_url=kana.avatar_url,
                    )
                    await ctx.send(embed=em2) 
    
    @commands.command()
    @commands.is_owner()
    async def remove(self, ctx, mem1: discord.User=None, mem2: discord.User=None):
        remove(mem1.id, mem2.id)
        await ctx.reply("`>> Successfully removed from database.`")

def setup(client):
    client.add_cog(Marry(client))
    print(">> Marry loaded")
