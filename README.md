# python_simple_image_cropper
Project born by intership.
I wrote the code really ugly because i had no time to add comments and spaces.
If anyone has doubt you can contact me.

#How to install
```bash
git clone https://github.com/edoaxyz/image_to_hOCR.git
cd image_to_hOCR
sudo python3 setup.py install
```


# To launch
#### From terminal
Build.py \<OutputName\> \<OCR\> \<Language\> \<DebugMode\> \<Reset\><br>
Outputname = the final name that the pdf will take (wrote without .pdf extension)<br>
OCR = true or false (T/t or F/f) [to analyze the text]<br>
Language = based on the languages you had downloaded<br>
DebugMode = true or false (T/t or F/f) [to see the elaborating process]<br>
Reset = true or false (T/t or F/f) [to clear all the data at the end]<br>
An Example<br><br>
**Build.py output t ita t f**<br>

#### From python
By running the Main.py and Launch the Elaborate Function<br>

# Objective
The objective was to create a script that could be used in a raspberry, which helps users to digitalize a book.<br>
The users only need to scan the pages even with a portable scanner **on an high contrast** background, create a folder in the data folder, add the images and then run the script called "Cropper.py".<br>
With a simple method the script finds the color changing on the axes, from the top and from the bottom then it crosses the data to create a rectangle in which the page should stay. Then it crops the page with a jump (to improve the looks of the output) and save the image on the out_cropper folder in the output folder.<br>
After the cropper, the user needs to run "Maker.py" to create a pdf from the images.<br>

# Colors & Algorithm
To define a rectangle you only need two points: the top-left one and the bottom-right one.<br>
So I need to find 4 coordinates (two abscissae and two ordinates). A way to solve this problem is to analyze pixel by pixel where the first big color changing appears. One from the top to the bottom, one from the left to the right, and the opposite two. (One from the bottom to the top and one from the right to the left).<br>
The color are written in BGR format thanks to the openCV library.<br>
#### old
The color changing is defined by the **Euclidian distance** [HERE](https://en.wikipedia.org/wiki/Color_difference):<br>
distance = square_root((R0 - R1) ** 2, (B0 - B1) ** 2, (G0 - G1) ** 2).<br>
If the distance is bigger than a certain P I can firmly say that there was a change!<br>
Added the rotation algorithm which recognise if an image is skew.<br>

## Debugging mode
I added a debug mode where you can see the algorithm results **graphically** and the math operations results.<br>

## Accepted extensions
Pratically all the *openCV* extensions :<br>
".jpeg", ".jpg", ".png", ".tif", ".tiff", ".bmp", ".dib", ".jpe", ".jp2", ".webp", ".pbm", ".pgm", ".ppm", ".sr", ".ras"<br>

## Optimizations
To improve the algorithm velocity and the reduce the effort, when it analyzes the image it reduces its dimensions (with a coefficent K = DIMENSIONS / 500) and after it finds the points it crops the original image from the two points coordinates multiplied by K.<br>
Also the jump is based on the coefficent K.<br>

### CHANGES
#### new v1.1
Removed some bugs to the cropper script, adapted to work on all platform.<br>
It load the images in grey scale so the distance its a simple difference.<br>
Added the Rotation Algorithm.<br>
Added the text output on a .txt.<br>
Fixed some unicode problem.<br>
#### new v1.2
Removed bugs.<br>
Now the reader will not make a txt file but an Hocr to improve the human correction helpness.<br>
Updated Main.py nd Reader.py<br>
Added Build.py to let you run the script easier<br>
