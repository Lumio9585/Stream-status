import discord
from discord.ext import commands
import os
from os import system
from colorama import Fore,init,Style
import pystyle
from pystyle import Colors, Colorate
os.system('cls & mode 54, 21')
title = 'Stream Status︱Version 1.0︱Lumio#9585'
system(f'title {title}')
print(Colorate.Horizontal(Colors.rainbow, ''' 

╔═╗╔╦╗╦═╗╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔═╗╔╦╗╦ ╦╔═╗
╚═╗ ║ ╠╦╝║╣ ╠═╣║║║  ╚═╗ ║ ╠═╣ ║ ║ ║╚═╗
╚═╝ ╩ ╩╚═╚═╝╩ ╩╩ ╩  ╚═╝ ╩ ╩ ╩ ╩ ╚═╝╚═╝

         Credit. : Lumio#9585                                                                        

'''))

token = input(f"[{Fore.RED}!{Style.RESET_ALL}] Input Token : ") 

bot = commands.Bot(command_prefix = "LUMIO")

status = input(f"[{Fore.RED}!{Style.RESET_ALL}] Input Status : ")
@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/leekbeats' 
    )
    print('Streaming: ' + status)
    os.system('cls')
    print(Colorate.Horizontal(Colors.rainbow, ''' 
    Enjoy <3
'''))
    await bot.change_presence(activity=stream)
    
bot.run(token, bot=False)  
