

#create function to grab all the words in word doc into a string var


import docx
import os

os.chdir('C:\\Users\\rkrall\\github\\AutomateTheBoringStuffWithPython\\14_ExcelWordPDF')


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('C:\\Users\\rkrall\\github\\AutomateTheBoringStuffWithPython\\14_ExcelWordPDF\\45_xdemo.docx'))
