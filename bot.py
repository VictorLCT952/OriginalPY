import discord
from discord.ext import commands
import os
import datetime

client = commands.Bot(command_prefix = '\\')

@client.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(client.user))
    print('-----------------------------------------------')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Membru")
    await member.add_roles(role)
    
 
@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Welcome to xSupportGamingx! You are the {len(list(member.guild.members))} member!", timestamp=datetime.datetime.utcfromtimestamp(1553629094))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=684096171874189561)

    await channel.send(embed=embed)

@client.event  
async def on_member_remove(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Just left our server, We are now {len(list(member.guild.members))} member!", timestamp=datetime.datetime.utcfromtimestamp(1553629094))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(id=684097193820553236)

    await channel.send(embed=embed)

client.run(os.getenv('TOKEN'))
