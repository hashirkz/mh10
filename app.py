from discord.ext import commands
import discord
import os 
from os import path
from utils import pdfminer_stuff
from utils import openai_model
from utils import event_generator
from dotenv import load_dotenv
from discord import app_commands
from dateutil import parser
import asyncio

load_dotenv('./.env')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
#bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


""" @bot.event
async def on_ready():
    print(f'running as {bot}') """


@client.event
async def on_message(message):
    # await client.process_commands(message)

    username = str(message.author)
    msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {msg}: ({channel})')

    if message.author == client.user:
        return

@client.event
async def on_ready():
    await tree.sync()
    print(f'discord bot running at {client}')

#@bot.command(aliases=['get_events'])
@tree.command(name="get_events", description="Create calendar events from a pdf!")
async def get_calendar(interaction: discord.Interaction, pdf: discord.Attachment):
    #if ctx.message.attachments: attachments = ctx.message.attachments[0]
    await interaction.response.defer()
    await asyncio.sleep(delay=4)
    try:
        text = pdfminer_stuff.read_pdf_url(pdf)
        splits = pdfminer_stuff.split_text(text)
        response = ""
        for text_split in splits:
            resp = openai_model.get_response(text_split)
            response += resp + ' '
        await interaction.followup.send(f'events are {response}')

        # new code
        
        # events_list = response.split("\n")
        # for i in range(len(events_list)):
        #     events_list[i] = events_list[i].split(": ")
        #     events_list[i][1] = parser.parse(events_list[i][1], fuzzy=True)
        #     events_list[i] = tuple(events_list[i])
        
        # event_generator.events_generator(events_list)
        # await ctx.send(files="./calendars/all_events.ics")
        
        
    except:
        #await ctx.message.channel.send(f'unable to read {attachments}')
        await interaction.followup.send(f'unable to read {pdf}')

@tree.command(name="summary", description="summarize the passed in document")
async def get_summary(interaction: discord.Interaction, pdf: discord.Attachment):
    #if ctx.message.attachments: attachments = ctx.message.attachments[0]
    await interaction.response.defer()
    await asyncio.sleep(delay=4)
    try:
        text = pdfminer_stuff.read_pdf_url(pdf)
        splits = pdfminer_stuff.split_text(text)
        response = ""
        for text_split in splits:
            resp = openai_model.get_response_summary(text_split)
            response += resp + ' '
        await interaction.followup.send(response)        
        
    except:
        #await ctx.message.channel.send(f'unable to read {attachments}')
        await interaction.followup.send(f'unable to read {pdf}')

@tree.command(name="ask", description="ask any prompt to chat gpt")
async def get_chat(interaction: discord.Interaction, prompt: str, pdf: discord.Attachment):
    #if ctx.message.attachments: attachments = ctx.message.attachments[0]
    await interaction.response.defer()
    await asyncio.sleep(delay=4)
    try:
        text = pdfminer_stuff.read_pdf_url(pdf)
        splits = pdfminer_stuff.split_text(text)
        response = ""
        for text_split in splits:
            resp = openai_model.get_response_ask(prompt, text_split)
            response += resp + ' '
        await interaction.followup.send(response)        
        
    except:
        #await ctx.message.channel.send(f'unable to read {attachments}')
        await interaction.followup.send(f'unable to read {pdf}')

# @tree.command()
# async def create_event(ctx, arg_str):
#     arg = arg_str.split(",")
#     for i in range(1, len(arg)):
#         arg[i] = parser.parse(arg[i], fuzzy=True)
#     event = [tuple(arg)]
#     event_generator.events_generator(event)
#     await ctx.send(files="./calendars/all_events.ics")


if __name__ == '__main__':
    client.run(DISCORD_BOT_TOKEN)