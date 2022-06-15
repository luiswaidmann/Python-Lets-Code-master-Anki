#Get tesseract from here: https://github.com/UB-Mannheim/tesseract/wiki

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from openpyxl import Workbook
import cv2
import matplotlib.pyplot as plt
from PIL import Image



#image = cv2.imread("files\img.PNG")
image = Image.open("files\wortschatz-gesicht-a-ca.PNG")

string = pytesseract.image_to_string(image)
print(string)

Exceldatei = Workbook()
Tabellenblatt = Exceldatei.active
Tabellenblatt['A1'] = string
Tabellenblatt.cell(row=2, column=2).value = 100
Exceldatei.save("PythonTest.xlsx")