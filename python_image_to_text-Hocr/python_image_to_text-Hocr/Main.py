###########################################################
import Cropper
import Reader
import os
###########################################################
phase = 0
###########################################################
def Elaborate(name, ocr = False, lang = "eng", debug = False):
    global phase
    nameDoc = name
    app_folder = os.path.dirname(__file__)
    fi = os.path.join(app_folder, "data")
    fo = os.path.join(app_folder, "output", "out_cropper")
    phase = 1
    Cropper.Crop(fi, fo, debug)
    if ocr:
        fi, fo = fo, os.path.join(app_folder, "output", "out_hocr")
        phase = 2
        Reader.Read(fi, fo, lang, debug, name)
    phase = 0
def getPhase():
    global phase
    if phase == 1: return (phase, Cropper.get_percentage())
    elif phase == 2: return (phase, Maker.get_percentage())
    else: return None
###########################################################
