# pySIC

pySIC (python_simple_image_cropper) is a python3  library  based on tesseract code to perform OCR of documents' images inside the DocumentiAperti project developed during internship of "CNR Tullio Buzzi" students.

## Requirements

The evironment of python3 ( pip3 , setuptools...)

```bash
sudo apt-get install libpng-dev libjpeg-dev libtiff-dev zlib1g-dev
sudo apt-get install gcc g++
sudo apt-get install autoconf automake libtool checkinstall

wget http://www.leptonica.org/source/leptonica-1.76.0.tar.gz
tar -zxvf leptonica-1.76.0.tar.gz
cd leptonica-1.76.0
./configure
make
sudo checkinstall
sudo ldconfig
```



tesseract ( > 3.05)

```bash
sudo apt-get install git
git clone https://github.com/tesseract-ocr/tesseract
cd tesseract
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
git clone https://github.com/tesseract-ocr/tessdata.git
sudo mv ~/tessdata/* /usr/local/share/tessdata/
```
Another way in ubuntu was done by using tesseract 4

```bash
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt-get install tesseract-ocr
```
If you want tesseract to handle every language type:
```bash
sudo apt-get install tesseract-ocr-all
```
or if you want to install only specific languages like English or Italian:
```bash
sudo apt-get install tesseract-ocr-eng tesseract-ocr-ita
```

## How to install pySIC on Ubuntu 16.04

For python dependencies see the requirements.txt file and/or launch in commandline:

```bash
git clone https://github.com/edoaxyz/image_to_hOCR.git
cd image_to_hOCR
sudo apt-get install libxml2-dev libxslt1-dev
sudo python3 setup.py install
```
Put your images or scans in ```./data``` directory and test it:

```python
import pySIC
pySIC.elaborate("merge")
pySIC.elaborate("merge_ocr",ocr=True,lang='ita')
```

## Aims

The objective was to create a script that could be used in a raspberry, which helps users to digitalize a book.
The users only need to scan the pages even with a portable scanner **on an high contrast** background, create a folder in the data folder, add the images and then run the script called "cropper.py".With a simple method the script finds the color changing on the axes, from the top and from the bottom then it crosses the data to create a rectangle in which the page should stay. Then it crops the page with a jump (to improve the looks of the output) and save the image on the out_cropper folder in the output folder. After the cropper, the user needs to run "maker.py" to create a pdf from the images.


# Colors & Algorithm

To define a rectangle you only need two points: the top-left one and the bottom-right one.
So I need to find 4 coordinates (two abscissae and two ordinates). A way to solve this problem is to analyze pixel by pixel where the first big color changing appears. One from the top to the bottom, one from the left to the right, and the opposite two. (One from the bottom to the top and one from the right to the left).
The color are written in BGR format thanks to the openCV library.
#### Old
The color changing is defined by the **Euclidian distance** [HERE](https://en.wikipedia.org/wiki/Color_difference):
distance = square_root((R0 - R1) ** 2, (B0 - B1) ** 2, (G0 - G1) ** 2).
If the distance is bigger than a certain P I can firmly say that there was a change!
Added the rotation algorithm which recognise if an image is skew.

## Debugging mode
I added a debug mode where you can see the algorithm results **graphically** and the math operations results.

## Accepted extensions
Pratically all the *openCV* extensions :
".jpeg", ".jpg", ".png", ".tif", ".tiff", ".bmp", ".dib", ".jpe", ".jp2", ".webp", ".pbm", ".pgm", ".ppm", ".sr", ".ras"

## Optimizations
To improve the algorithm velocity and the reduce the effort, when it analyzes the image it reduces its dimensions (with a coefficent K = DIMENSIONS / 500) and after it finds the points it crops the original image from the two points coordinates multiplied by K.
Also the jump is based on the coefficent K.

# References
https://www.linux.com/blog/using-tesseract-ubuntu

### CHANGELOG
#### v0.0.1
 - Removed some bugs to the cropper script, adapted to work on all platform.
 - It load the images in grey scale so the distance its a simple difference.
 - Added the Rotation Algorithm.
 - Added the text output on a .txt.
 - Fixed some unicode problems.

#### v0.0.2
 - Removed bugs.
 - Now the reader will not make a txt file but an Hocr to improve the human correction helpness.
 - Updated Main.py nd Reader.py
 - Added Build.py to let you run the script easier
