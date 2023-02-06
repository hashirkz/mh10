import openai
import os
from dotenv import load_dotenv

load_dotenv('./.env')
OPENAI_API_TOKEN = os.getenv("OPENAI_API_TOKEN")

# sets the api key
openai.api_key = OPENAI_API_TOKEN


def get_response(pdf_text):
    """
    Takes in string parsed from pdf with all escape characters removed and returns the model's reponse
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What are the important dates for midterms, quizes, homework, exams, or assignments from the following text? " + pdf_text + " give the response in the following format - Event Name:MM/DD/YYYY. Exlude times of day. Take note of start dates and end dates. Make each event on a new line.",
        temperature=0.05,
        max_tokens=200,
        logit_bias={"22622": 1, "4354": 1, "39": 1, "54": 1, "28718": 1, "6433": 1, "8021": 1, "16747": 1, "40781": 1,
                    "900": 1, "3705": 1, "3109": 1, "321": 1, "4507": 1, "528": 1}
    )

    return response.choices[0].text


def get_response_summary(pdf_text: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="please summarize the following text" + pdf_text,
        max_tokens=200,
    )

    return response.choices[0].text


def get_response_ask(prompt: str, pdf_text: str) -> str:
    if len(pdf_text) > 6000: pdf_text = pdf_text[:6000]

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt + ': ' + pdf_text,
        max_tokens=500,
    )

    return response.choices[0].text
