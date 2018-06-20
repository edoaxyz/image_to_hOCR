###########################################################
import pySIC.cropper
import pySIC.reader
import os
import sys
###########################################################
phase = 0
###########################################################
if sys.version_info[0] != 3:
    print("This module works only with Python 3!")

def create_dir(directory):
    if not os.path.exists(directory):
           os.makedirs(directory)

def init_wdirs(): 
    create_dir('data')
    create_dir('output/out_cropper')
    create_dir('output/out_hocr')


def elaborate(name, ocr = False, lang = "eng", debug = False):
    global phase
    nameDoc = name
    app_folder = os.getcwd()
    fi = os.path.join(app_folder, "data")
    fo = os.path.join(app_folder, "output", "out_cropper")
    phase = 1
    cropper.Crop(fi, fo, debug)
    if ocr:
        fi, fo, foPDF = fo, os.path.join(app_folder, "output", "out_hocr"), os.path.join(app_folder,"output")
        phase = 2
        reader.Read(fi, fo, foPDF, lang, debug, name)
    phase = 0

def getPhase():
    global phase
    if phase == 1: return (phase, cropper.get_percentage())
    elif phase == 2: return (phase, reader.get_percentage())
    else: return None
###########################################################
