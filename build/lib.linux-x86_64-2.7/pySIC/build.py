import sys
import Main

#program name, output_name, ocr, language, debug
l = ["", "", False, "", False]

for i, ar in enumerate(sys.argv, 0):
    if ar.upper() == "F": ar = False
    elif ar.upper() == "T": ar = True
    l[i] = ar

Main.Elaborate(l[1], ocr = l[2], lang = l[3], debug = l[4])
