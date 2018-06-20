###############################################################
import os
import cv2
import math
import numpy as np
from scipy.ndimage import interpolation as inter
from scipy.ndimage import rotate
###############################################################
C_percentage = 0
ACCEPTED_EXTENSIONS = (".jpeg", ".jpg", ".png", ".tif", ".tiff", ".bmp", ".dib", ".jpe", ".jp2", ".webp", ".pbm", ".pgm", ".ppm", ".sr", ".ras")
###############################################################
def euclidian_distance(first, second):
    return math.sqrt(sum([pow(max(x, y) - min(x, y), 2) for x, y in zip(first, second)]))
def color_difference(first, second, precision = 100):
    return euclidian_distance(first, second) > precision
def precision(arr, angle):
    hit = np.sum(inter.rotate(arr, angle, reshape = False, order = 0), axis = 1)
    prec = np.sum((hit[1:]-hit[:-1])**2)
    return prec
def rotateImage(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(255,255,255))
    return result
def Crop(abs_folder_in, abs_folder_out, debug):
    global C_percentage
    images_list = [i for i in os.listdir(abs_folder_in) if i.endswith(ACCEPTED_EXTENSIONS) and i[:2] != "ad"]
    if debug: print("\n".join(images_list))
    images_list = sorted(images_list, key = lambda i: int(i[:-4]))
    for c, image_path in enumerate(images_list, 1):
        original_image = cv2.imread(os.path.join(abs_folder_in, image_path), 0)
        sheet = cv2.resize(original_image, (0, 0), fx = 0.125, fy = 0.125)
        ret, sheet = cv2.threshold(sheet, 127, 255, cv2.THRESH_BINARY)
        wd, ht = sheet.shape
        pix = np.array(sheet, np.uint8)
        bin_img = 1 - (pix / 255.0)
        limit, delta = 10, 1
        angles = np.arange(-limit, limit+delta, delta)
        scores = [precision(bin_img, angle) for angle in angles]
        best = angles[scores.index(max(scores))]
        original_image = rotateImage(cv2.imread(os.path.join(abs_folder_in, image_path)), best)
        w, h, z = original_image.shape
        K = 500 / max(w, h)
        resized_image = cv2.resize(original_image, (0, 0), fx = K, fy = K)
        w, h, z = resized_image.shape
        mx, my = int(w / 2), int(h / 2)
        startx = 0
        starty = 0
        endx = w
        endy = h
        for i in range(1, w):
            if color_difference(resized_image[i, my], resized_image[i - 1, my]):
                startx = i
                break
        for i in range(w - 2, 0, -1):
            if color_difference(resized_image[i, my], resized_image[i + 1, my]):
                endx = i
                break
        for i in range(1, h):
            if color_difference(resized_image[mx, i], resized_image[mx, i - 1]):
                starty = i
                break
        for i in range(h - 2, 0, -1):
            if color_difference(resized_image[mx, i], resized_image[mx, i + 1]):
                endy = i
                break
        if endx <= startx:
            endx = w
        if endy <= starty:
            endy = h
        startx, starty, endx, endy = int(startx * (1 / K)), int(starty * (1 / K)), int(endx * (1 / K)), int(endy * (1 / K))
        jump = int(1 / K * 10)
        if debug:
            print("Angle : ", best)
            print("K : ", K, " jump : ", jump)
            print("(", startx, ", ", starty, ") -> (",  endx, ", ", endy, ")")
            print("Saving...")
        if (endx-jump) - (startx+jump) < (w*K)/3 or (endy-jump) - (starty+jump) < (h*K)/3:
            cv2.imwrite(os.path.join(abs_folder_out, str(c) + ".jpg"), original_image)
        else:
            cv2.imwrite(os.path.join(abs_folder_out, str(c) + ".jpg"), original_image[startx + jump : endx - jump, starty + jump : endy - jump])
        if debug: print("Done ", c, " of ", len(images_list))
        C_percentage += 1 / len(images_list)
    C_percentage = 0
def get_percentage():
    global C_percentage
    return C_percentage
###############################################################
