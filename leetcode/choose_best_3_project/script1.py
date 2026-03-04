import re
from PyPDF2 import PdfReader


path = r'c:\\Users\\hi\\Downloads\\oreillyBooks\\The Big Book of Small Python Projects.pdf'

reader = PdfReader(path)

print('pages', len(reader.pages))
for i in range(min(25, len(reader.pages))):
    
    text = reader.pages[i].extract_text() or ''
    text = re.sub(r'\s+', ' ', text)
    print(f'---PAGE {i+1}---')
    print(text[:120])
