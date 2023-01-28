import cohere
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import datefinder


# will probably move these functions to a utils folder later

# loading api keys / tokens globally
load_dotenv()
COHERE_API_TOKEN = os.getenv('COHERE_API_TOKEN')

# tries to parse the pdf at *path and returns the text contained in the pdf
def pdf_to_text(path: str, max_length: int=2000) -> str:
    try:
        pdf = PdfReader(path)
        text = ''.join([page.extract_text() for page in pdf.pages])

        return text[:2000] if len(text) > 2000 else text

    except FileNotFoundError:
        print(f'unable to read ./{path}')
        raise FileNotFoundError

# formats a cohere training example by appending the date labels *event: due date to the pdf_text
def cohere_prompt(pdf_text: str, date_labels: str, test: bool=False) -> str:
    pdf_text, date_labels = pdf_text.rstrip(' \n').replace('\n', ''), date_labels.rstrip(' \n').replace('\n', ' ')
    return f'{pdf_text}\n{date_labels}\n--\n' if not test else f'{pdf_text}\nextract the due date and event from the text:\n'


if __name__ == '__main__':
    train1 = pdf_to_text('./pdfs/mgu_math324_w23.pdf')
    label1 = f'''
extract the due date and event from the text: 
assignment 1: jan 27 11:59pm
assignment 2: feb 17 11:59pm
midterm exam: feb 22 10:00am
assignment 3: mar 10 11:59pm
assignment 4: mar 24 11:59pm
final exam: apr 14-28'''

    header = 'this program extracts the due dates from text:\n'
    test1 = 'Jan 09 Chap. 1 Course syllabus & Introduction to transport processes 2 Jan 16 Chap. 6 HW 1 Assigned Mass transport relations & diffusion'
    test1_label = ''
    prompt1 = header + cohere_prompt(train1, label1) + cohere_prompt(test1, test1_label, test=True)
    prompt1 = prompt1.rstrip('-\n')
    
    prompt2 = f"""  
        This program extracts due dates from text

        Midterm date Tues, March 7, 2023 
        extract the due date and title from the text: Miderm: Tues, March 7, 2023
        --  
        Jan 09 Chap. 1 Course syllabus & Introduction to transport processes 2 Jan 16 Chap. 6 HW 1 Assigned Mass transport relations & diffusion
        extract the due date and title from the text: Jan 16: HW 1 Assigned
        --  
        Jan 23 Chap. 6 Groups and topic chosen Unsteady state diffusion & molecular mechanisms 4 Jan 30 Chap. 7 HW 1 Due Diffusion + convection
        extract the due date and title from the text: Jan 16: HW 1 Due

        --  
        On-line quiz January 30 30 minutes 3-9pm window 10% 
        extract the due date and title from the text: On-line quiz: January 30

        --  
        Mid-term Tuesday Feb 21 In class 30% 
        extract the due date and title from the text:
    """

    co = cohere.Client(COHERE_API_TOKEN)
    response = co.generate(  
        model='xlarge',  
        prompt = prompt1,  
        max_tokens=40,  
        temperature=0.6,  
        stop_sequences=["--"],
    )

    event = response.generations[0].text
    print(event)