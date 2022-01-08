import discord
from discord.ext import commands
import io

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ds'])
    async def dumpservers(self, ctx):
        timestamp = discord.utils.utcnow().strftime("%Y-%m-%d %H.%M")
        server_file = "Servers-{}.txt".format(timestamp)

        mess = await ctx.send(
            content=f"Saving servers to **{server_file}**...",
        )

        msg = ""
        for server in self.client.guilds:
            msg += "Name:    " + server.name + "\n"
            msg += "ID:      " + str(server.id) + "\n"
            msg += "Owner:   " + str(server.owner) + "\n"
            msg += "Members: " + str(len(server.members)) + "\n"
            msg += "\n\n"

        data = io.BytesIO(msg.encode("utf-8"))

        await mess.edit(content="Uploading `{}`...".format(server_file))
        await ctx.send(file=discord.File(data, filename=server_file))
        await mess.edit(
            content=f"✅ Uploaded `{server_file}`."
        )

def setup(client):
    client.add_cog(Owner(client))
    print(">> Owner Loaded.")
