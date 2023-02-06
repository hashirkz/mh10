from pdfminer.high_level import extract_text
import re
from io import BytesIO
import requests

def read_pdf_url(url)->str:
    response = requests.get(url)
    data = response.content
    with BytesIO(data) as d:
        text = extract_text(d)
    return re.sub(r'\s+', ' ', text)

def parse_pdf(pdf_file)->str:
    text = extract_text(pdf_file)
    return re.sub(r'\s+', ' ', text)

def split_text(pdf_text)->list:
    parts = []
    toks = pdf_text.split(' ')

    if len(toks) >= 2000:
        split1 = toks[:int(len(toks)/2)] 
        split2 = toks[int(len(toks)/2):]
        parts.append(' '.join(split1))
        parts.append(' '.join(split2))
    else:
        return [pdf_text]
    return parts
