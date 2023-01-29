import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env')
OPENAI_API_TOKEN = os.getenv("OPENAI_API_KEY")

#sets the api key
openai.api_key = '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'

def get_response(pdf_text):
    """
    Takes in string parsed from pdf with all escape characters removed and returns the model's reponse
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What are the important dates for midterms, quizes, homework, exams, or assignments from the following text? " + pdf_text + " do not include anything except the important dates and their titles",
        temperature=0.3,
        max_tokens=200)
    
    return response.choices[0].text

def format_dates(first_text):
    """
    Takes in a string with all escape characters removed and isolates the dates, formatting them into MM/DD/YYYY
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="remove everything in the following text except for dates which are formatted into MM/DD/YYYY: " + first_text,
        temperature=0.3,
    )
