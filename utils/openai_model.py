import openai
import os

OPENAI_API_TOKEN = os.getenv("OPENAI_API_KEY")

#sets the api key
openai.api_key = OPENAI_API_TOKEN

def get_response(pdf_text):
    """
    Takes in string parsed from pdf with all escape characters removed and returns the model's reponse
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="What are the important dates for midterms, quizes, homework, exams, or assignments from the following text? " + text + " do not include anything except the important dates and their titles",
        temperature=0.3,
        max_tokens=200)
    
    return response.choices[0].text

