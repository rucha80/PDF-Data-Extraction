# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:25:28 2020

@author: 3kt
"""
path = r'C:\Users\3kt\Downloads\karunyahaloi01.pdf'
path1 = r"C:\Users\3kt\Downloads\RuchaSawarkar.pdf"
path2 = r"C:\Users\3kt\Downloads\resume.pdf"

#Using PyPDF2
# importing required modules  
import PyPDF4    
# creating a pdf file object  
pdfFileObj = open(path1, 'rb')    
# creating a pdf reader object  
pdfReader = PyPDF4.PdfFileReader(pdfFileObj)    
# printing number of pages in pdf file  
print(pdfReader.numPages)    
# creating a page object  
pageObj = pdfReader.getPage(0)    
pypdf2_text = pdfReader.getPage(0).extractText()
# extracting text from page  
for i in range(pdfReader.numPages):
    pypdf2_text +=pdfReader.getPage(i).extractText()
#print(pageObj.extractText())    
# closing the pdf file object  
pdfFileObj.close()  

#using Tika
from tika import parser # pip install tika
raw = parser.from_file(path)
tika_text = raw['content']

import codecs
#using Textract
import textract
textract_text = textract.process(r'C:\Users\3kt\Downloads\karunyahaloi01.pdf')
textract_str_text = codecs.decode(textract_text)


#Usinf pymupdf
import fitz  # this is pymupdf
with fitz.open(path2) as doc:
    pymupdf_text = ""
    for page in doc:
        pymupdf_text += page.getText()
#print(pymupdf_text)



#Using PDFminer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)
    text = retstr.getvalue()
    fp.close()
    device.close()
    retstr.close()
    return text

pdf_miner_text = convert_pdf_to_txt(path2)

#Using PDFtotext
import pdftotext
# Load your PDF
with open(path1, "rb") as f:
    pdf = pdftotext.PDF(f)
# Read all the text into one string
pdftotext_text = "\n\n".join(pdf)
#print("\n\n".join(pdf))

def saveText(texto, fileName, nameLib):
    """Save the text in a file
    Arguments:xc
        texto {str} -- text in str format
        fileName {str} -- filename (without path in this code)
        nameLib {str} -- name of extractor project
    """    
    arq = open(fileName + "-" + nameLib + ".txt", "w")
    arq.write(texto)        
    arq.close()
    
saveText(pdftotext_text, r"C:\Users\3kt\Desktop\Rucha\Similarity\pinku.txt", "pdftotext")


#using Tabula
import tabula
df = tabula.read_pdf(path, pages='all')