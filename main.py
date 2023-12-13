
import pytesseract
from PIL import Image
import PIL.Image
import cv2

"""""
Page segmentation modes:
O Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD. ‘
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of textJ
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possible in no particular order.
12 Sparse text with OSD.
13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract—specific.
"""

"""
OCR Engine modes:

Legacy engine only.
Neural nets LSTM engine only.
Legacy + LSTM engines.
Default, based on what is available.
"""
myconfig = r"--psm 6 --oem 3 "
text = pytesseract.image_to_string(PIL.Image.open("marselka.jpeg"), config=myconfig)
file = open('myfile.txt', 'w')
file.write(text)
file.close()
print()
with open('myfile.txt') as f:
    lines = f.readlines()
    for i in lines:
        print(i, end='')