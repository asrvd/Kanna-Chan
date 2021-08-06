import discord
from discord.ext import commands
import json
import requests
from decouple import config
import random

UNSPLASH_KEY = str(config("UNSPLASH_KEY"))

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.kana_id = 857835279259664403

    @commands.command()
    async def woof(self, ctx):
        kana = self.client.get_user(self.kana_id)
        url = f"https://api.unsplash.com/search/photos/?client_id={UNSPLASH_KEY}"

        page = random.randint(1, 333)
        pic_no = random.randint(1,20)
        querystring = {"page":str(page), "per_page":"100", "query":"dog"}
        response = requests.request("GET", url, params=querystring)

        text = response.text
        json_data = json.loads(text)
        url = json_data["results"][pic_no]["urls"]["regular"]
        
        embed = discord.Embed(title="woof, woof!", color=0x2e69f2)
        embed.set_image(url=url)
        embed.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def meow(self, ctx):
        kana = self.client.get_user(self.kana_id)
        url = f"https://api.unsplash.com/search/photos/?client_id={UNSPLASH_KEY}"

        page = random.randint(1, 333)
        pic_no = random.randint(1,20)
        querystring = {"page":str(page), "per_page":"100", "query":"cat"}
        response = requests.request("GET", url, params=querystring)

        text = response.text
        json_data = json.loads(text)
        url = json_data["results"][pic_no]["urls"]["regular"]
        
        embed = discord.Embed(title="meow, meow!", color=0x2e69f2)
        embed.set_image(url=url)
        embed.set_footer(
            text=f"Kanna Chan",
            icon_url=kana.avatar_url,
        )
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Image(client))
  print(">> Images loaded")