import discord
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
import os
import datetime
# Intents 객체 생성
intents = discord.Intents.default()

# 모든 이벤트 활성화
intents.all()

# 봇 클라이언트 생성 시 intents 옵션으로 intents 전달
bot = commands.Bot(command_prefix='.', intents=intents, application_id='id')

@bot.event
async def on_ready():
    print('Online.')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message[0] == '.':
        return
    if message.author == bot.user:
        return
    await message.channel.send("hello")
    
async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start('token')

asyncio.run(main())