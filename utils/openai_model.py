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
        prompt="What are the important dates for midterms, quizes, homework, exams, or assignments from the following text? " + pdf_text + " give the response in the following format - Event Name:MM/DD/YYYY. Exlude times of day. Take note of start dates and end dates. \
        Also provide the course code such as 'BIEN 340' at the top of the response - the course code is located at the beginning of the text.",
        temperature=0.01,
        max_tokens=200,
        logit_bias={"22622": 1 , "4354": 1, "39": 1, "54": 1, "28718": 1, "6433": 1, "8021": 1, "16747": 1, "40781": 1, "900": 1, "3705": 1, "3109": 1, "321": 1, "4507": 1 , "528": 1} 
    )
    
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
