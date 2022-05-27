import discord
from discord.ext import commands
import os
from os import system
from colorama import Fore,init,Style
os.system("cls")
title = 'Stream Status︱Version 1.0︱Lumio#9585'
system(f'title {title}')
print(f"""{Fore.MAGENTA}

  _, ___ __, __,  _, _, _    _, ___  _, ___ _,_  _,
 (_   |  |_) |_  / \ |\/|   (_   |  / \  |  | | (_ 
 , )  |  | \ |_  |~| |  |   , )  |  |~|  |  | | , )
  ~   ~  ~ ~ ~~~ ~ ~ ~  ~    ~   ~  ~ ~  ~  `~'  ~ 
                Credit : Lumio#9585                                                                        

{Style.RESET_ALL}""")

token = input(' Enter Token \n > ') 

bot = commands.Bot(command_prefix = "LUMIO")

status = input('Enter Status \n > ')

@bot.event
async def on_connect():
    stream = discord.Streaming(
        name = status,
        url = 'https://www.twitch.tv/leekbeats' 
    )
    print('Streaming: ' + status)
    await bot.change_presence(activity=stream)
    
bot.run(token, bot=False)  