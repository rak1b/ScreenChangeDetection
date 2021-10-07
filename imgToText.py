# https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210811.exe

import pytesseract

from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rak13\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def getText(path):
    value = Image.open(path)
    text = pytesseract.image_to_string(value)
    return text
