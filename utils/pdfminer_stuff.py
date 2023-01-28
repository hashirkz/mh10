from pdfminer.high_level import extract_text
import re

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
        return list(pdf_text)
    return parts
