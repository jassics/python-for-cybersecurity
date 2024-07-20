# brew install zbar
# Ubuntu: sudo apt-get install zbar-tools or libzbar
# pip install pyzbar
# pip install pillow
from pyzbar.pyzbar import decode
from PIL import Image

d = decode(Image.open("fm-qr-code.png"))
# print(d)
print(d[0].data.decode())
