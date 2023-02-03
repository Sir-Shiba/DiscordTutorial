import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

#   loading env and getting token
load_dotenv()
token = os.getenv("token")

#   discord intents
client = commands.Bot(command_prefix="=", intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('ping pong mode'))
    await client.tree.sync()
    print("Successful Start")

@client.event
async def on_message(ctx):
    if ctx.content == 'ping':
        ctx.message.reply("pong!")

#   this is a funny verison of pong
@client.event
async def on_message(ctx):
    if ctx.content == 'start pong':
        cont = True
        await ctx.channel.send("ping!")
        while cont:
            msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
            if msg.content == "pong":
                await ctx.channel.send("ping!")
            else:
                await ctx.channel.send("why you stop :(, how can you do this to me")
                cont = False

client.run(token)

