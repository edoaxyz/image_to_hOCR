############################################################
import pytesseract
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont
#############################################################
R_percentage = 0
if "TESSERACT_EXEC" in os.environ:
    pytesseract.pytesseract.tesseract_cmd = os.environ["TESSERACT_EXEC"]
#############################################################
def real(t):
    return "".join([c for c in t if c.isalnum()])
def Read(abs_folder_in, abs_folder_out, abs_folder_out_pdf, lang, debug, name):
    global  R_percentage
    app_folder = os.path.dirname(__file__)
    s = sorted([int(i[:-4]) for i in os.listdir(abs_folder_in) if i.endswith(".jpg")])
    images_list = [os.path.join(abs_folder_in, str(i) + ".jpg") for i in s]
    for c, img_name in enumerate(images_list, 0):
        if debug: print("Creating hOCR")
        pytesseract.pytesseract.run_tesseract(img_name, os.path.join(abs_folder_in, str(s[c])), lang = lang, extension = "", config = "hocr")
        if debug: print("Done ", c+1, " of ", len(images_list))
        R_percentage += 1 / len(images_list)
    if debug: print("Creating Pdf from Hocr and images")
    os.system("hocr-pdf --savefile " + os.path.join(abs_folder_out_pdf, name + ".pdf" ) + " " + abs_folder_in)
    if debug: print("Moving the hocr to their folder")
    for i, n in zip(images_list, s):
        os.rename(i[:-4]+".hocr", os.path.join(abs_folder_out, str(n)+".hocr"))
    R_percentage = 0
def get_percentage():
    global R_percentage
    return R_percentage
###############################################################
