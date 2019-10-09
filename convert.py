#!/usr/local/bin/python3
import sys
import os
from PIL import Image

try:
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
except IndexError:
    print("You must supply a valid source and destination directory: convert-to-png.py <source directory> <destination directory>")
    sys.exit(2)

for filename in os.listdir(src_dir):
    if filename.endswith('.png'):
        im = Image.open(src_dir + filename)
        rgb_im = im.convert('RGB')
        new_filename = filename.strip('.png')
        rgb_im.save(dst_dir + new_filename+'.jpeg')
        print('Saved converted file: '+dst_dir+new_filename+'.jpeg')
