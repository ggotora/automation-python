#!/usr/bin/env python3

import os 
from PIL import Image
filename = "buildings.jpg"
size =  600, 400

path = "images/"
for file in os.listdir(path):
    if file.endswith('.tiff'):
        f, e = os.path.splitext(file)
        print(f)
        outfile = path + f + ".jpeg"
        with Image.open(path +file) as im:
            im.convert('RGB')
            im.thumbnail(size)
            print(file, im.format, f"{im.size}x{im.mode}")
            im.save(outfile)