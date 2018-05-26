# -*- coding: utf-8 -*-
import os
import tempfile
import imghdr
import shutil

from AppKit import NSPasteboard, NSPasteboardTypePNG,\
        NSPasteboardTypeTIFF, NSPasteboardTypeString,\
        NSFilenamesPboardType

# image_file, need_format, need_compress
NONE_IMG = (None, False, None)

def get_paste_img_file():

    pb = NSPasteboard.generalPasteboard()
    data_type = pb.types()

    supported_image_format = (NSPasteboardTypePNG, NSPasteboardTypeTIFF)
    if NSFilenamesPboardType in data_type:
        # file in clipboard
        img_path = pb.propertyListForType_(NSFilenamesPboardType)[0]
        img_type = imghdr.what(img_path)
        return img_path
        
if __name__ == '__main__':
    print(get_paste_img_file())
