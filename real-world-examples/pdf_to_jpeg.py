#!/usr/bin/python

# In case of error related to module not found use below steps:
# pip3 install pdf2image
# Poppler is required by pdf2image to work.
#   Mac: brew install poppler
#   Linux: sudo apt-get install python-poppler
#   Windows: https://poppler.freedesktop.org/
# If you still get no module found error try this in Mac:
#    python3 -m pip install pdf2image --user

from pdf2image import convert_from_path

# filename. Change the file-name.pdf to actual pdf file name.
pdf_file = "Python3-Specialization-XK7XRMUDJZAH.pdf"

# Let the conversion begine
pages = convert_from_path(pdf_file)

# replace .pdf with blank so that we can add image extension while saving it.
img_file = pdf_file.replace(".pdf","")

# Saving pages in jpeg format
count = 0
for page in pages:
    count +=1
    jpeg_file = img_file + "-" + str(count) + ".jpeg"
    page.save(jpeg_file, 'JPEG')
