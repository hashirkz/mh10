import openai
import os

OPENAI_API_TOKEN = os.getenv("OPENAI_API_KEY")

def get_summary(pdf_text)->str:
    """
    Summarizes an imported pdf_text with the intent to teach.
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Summarize the ideas in the following text taken from lecture slides: " + pdf_text,
        temperature=0.5,
        max_tokens=500)

    return response.choices[0].text