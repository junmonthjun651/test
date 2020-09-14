import asyncio
import discord
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup
import requests
import time
import random
import traceback
import re
import youtube_dl
import os




bot = commands.Bot(command_prefix='^')


            
            



            
            

@bot.event
async def on_ready():
      print("로딩완료")
      game_1 = discord.Game("셧더법껌")
      await bot.change_presence(status=discord.Status.online, activity=game_1)
      
@bot.command(name="야추")
async def mola(ctx, args):
      if args == "시작":
            await ctx.send("주사위를 던집니다")
      else:
            await ctx.send("**[시작, 던지기, 가져오기, 꺼내오기]**중에서 입력해 주세요")
@mola.error
async def mola_error(ctx, error):
      if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("**[시작, 던지기, 가져오기, 꺼내오기]**중에서 입력해 주세요")
            













bot.run("token")
