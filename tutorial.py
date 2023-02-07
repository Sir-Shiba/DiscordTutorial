#   necessary imports
import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

#   loading env and getting token
load_dotenv()
token = os.getenv("token")

#   discord intents
client = commands.Bot(command_prefix="=", intents=discord.Intents.all())

#   this chunk defines what you want to happen when the bot starts up
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('This is a bot'))
    await client.tree.sync()
    print("Successful Start")

#   ways to send message
@client.event
async def on_message(ctx):
    print(f"Channel: {ctx.channel}")
    print(f"Channel Id: {ctx.channel.id}")
    print(f"Author: {ctx.author}")
    print(f"Author Id: {ctx.author.id}")
    print(f"Content: {ctx.content}")
    #   pinging
    if ctx.content == 'ping':
        await ctx.reply("pong!")
    #   message sending
    if ctx.content == 'trial':
        await ctx.channel.send("Messaging the Channel")
        await ctx.channel.send(f'Mentioning <@{ctx.author.id}>')
        await ctx.channel.send(f'Mentioning {ctx.author.mention}')
        await ctx.reply("Replying to User")
        await ctx.author.send("Private message")
    #   embeds
    elif ctx.content == 'embed':
        embed=discord.Embed(title="This is an embed", description="Description for the embed")
        embed.set_image(url="https://www.myinstants.com/media/instants_images/rickroll.png")
        embed.set_author(name="Rick Roll", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        embed.add_field(name="Field 1", value="Hello", inline=True)
        embed.add_field(name="Field 2", value="Hello", inline=True)
        embed.add_field(name="Field 3", value="Hello", inline=False)
        embed.set_footer(text="Page 1 of 1")
        await ctx.channel.send(embed=embed)
    await client.process_commands(ctx)

@client.command()
async def echo_first(ctx, arg):
    await ctx.send(arg)

@client.command()
async def echo_all(ctx, *, arg):
    await ctx.send(arg)

@client.command(\
    aliases=["plus", "+"],\
    brief='Addition',\
    description='This adds two numbers')
async def add(ctx, a: int , b: int = commands.parameter(description="Give me a number")):
    await ctx.send(a + b)

@client.command()
async def dm(ctx, member: commands.MemberConverter, *, msg):
    await member.send(msg)

class Praise(commands.Converter):
    async def convert(self, ctx, arg):
        to_slap = random.choice(ctx.guild.members)
        return f'{ctx.author} praised {to_slap} because *{arg}*'

@client.command()
async def praise(ctx, *, reason: Praise):
    await ctx.send(reason)

@client.tree.command(name="user_info", description="Retrieves User Information")
async def userinfo(interaction: discord.Interaction, member: discord.User=None):
    if member == None:
        member = interaction.user
    embed = discord.Embed(title="User Info", description=f"Here's the User Info do {member.mention}", color = discord.Color.blue())
    embed.set_thumbnail(url=member.avatar)
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Name', value=member.name)
    embed.add_field(name='Nick', value=member.display_name)
    embed.add_field(name='Bot?', value=member.bot)
    await interaction.response.send_message(embed=embed)

#   runs your bot
client.run(token)