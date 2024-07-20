# pip install pyqrcode
# if it gives error as png moudle not found, install it using `pip install pypng`
# pip install pillow for PIL module
import pyqrcode
from PIL import Image

s = "https://www.flexmind.co/tutorials/az-400-certification-course-devops/"
#s = "Name: Sanjeev Jassi\nSite: https://www.aliencoders.org/\nLocation: Bangalore"
url = pyqrcode.create(s)

img = "fm-qr-code.png"
url.png(img, scale=10)

#opening image
im=Image.open(img)
im.show()
