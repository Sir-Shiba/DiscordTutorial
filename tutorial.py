#   necessary imports
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
    await client.tree.sync()
    print("Sucess")
    

@client.tree.command(name='hello')
async def hello(Interaction: discord.Interaction):
    await Interaction.response.send_message(content="Hi", ephemeral=True)

#   runs the bot

client.run(token)