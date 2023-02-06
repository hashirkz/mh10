import os
from utils import pdfminer_stuff
from utils import openai_model
from utils import event_generator
from dotenv import load_dotenv
from dateutil import parser
import interactions
from interactions.ext.files import command_send

load_dotenv('./.env')
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = interactions.Client(DISCORD_BOT_TOKEN)


@bot.command(
    name='get_events',
    description='Upload a pdf to extract event dates into an ICS calendar file',
    options=[
        interactions.Option(
            name="pdf",
            description="Add your course syllabus pdf",
            type=interactions.OptionType.ATTACHMENT,
            required=True,
        ),
        interactions.Option(
            name="course",
            description="Add your course code",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def get_calendar(ctx: interactions.CommandContext, pdf: interactions.OptionType.ATTACHMENT, course: str):
    await ctx.send(f"You attached '{pdf.filename}'!")
    text = pdfminer_stuff.read_pdf_url(pdf.url)
    splits = pdfminer_stuff.split_text(text)
    response = ''
    for text_split in splits:
        resp = openai_model.get_response(text_split)
        response += resp + ' '
    events_list = response.split('\n')
    events_list = list(filter(None, events_list))
    new_events_list = [course + ' ' + event for event in events_list]
    cleaned = []
    for i in range(len(new_events_list)):
        split = new_events_list[i].split(": ")  # split to list [value, time]
        try:
            split[1] = parser.parse(split[1], fuzzy=True)  # try to make date time object
            cleaned.append(tuple(split))  # add tuple to list
        except parser.ParserError:
            pass
    event_generator.events_generator(cleaned)
    data = open('calendars/all_events.ics', 'rb')
    await ctx.send(f'Your events are: {response}')
    file = interactions.File(filename='events.ics', fp=data)
    await command_send(ctx, "Here is your file: ", files=file)

@bot.command(
    name='ask',
    description='ask me anything about a pdf',
    options=[
        interactions.Option(
            name="pdf",
            description="Add pdf",
            type=interactions.OptionType.ATTACHMENT,
            required=True,
        ),
        interactions.Option(
            name="prompt",
            description="enter your prompt",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def get_chat(ctx: interactions.CommandContext, pdf: interactions.OptionType.ATTACHMENT, prompt: str):
    await ctx.send(f"Analyzing '{pdf.filename}'!")
    try:
        text = pdfminer_stuff.read_pdf_url(pdf.url)
        response = openai_model.get_response_ask(prompt, text)
        await ctx.send(response)

    except:
        await ctx.send(f'unable to read {pdf.filename}')


if __name__ == '__main__':
    bot.start()
