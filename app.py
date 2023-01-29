from discord.ext import commands
import discord
import os 
from os import path
from utils import pdfminer_stuff
from utils import openai_model
from dotenv import load_dotenv

load_dotenv('./.env')

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'running as {bot}')


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    username = str(message.author).split('#')[0]
    msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {msg}: ({channel})')

    if message.author == bot.user:
        return



@bot.command(aliases=['get_events'])
async def get_calendar(ctx):
    attachments = ctx.message.attachments[0]
    try:
        text = pdfminer_stuff.read_pdf_url(attachments)
        splits = pdfminer_stuff.split_text(text)
        response = ""
        for text_split in splits:
            resp = openai_model.get_response(text_split)
            response += resp + ' '
            print(text_split[:100])
        await ctx.message.channel.send(f'events are {response}')
    except FileNotFoundError:
        await ctx.message.channel.send(f'unable to read {attachments}')

    

if __name__ == '__main__':
    bot.run(DISCORD_BOT_TOKEN)