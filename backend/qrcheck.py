from pyzbar.pyzbar import decode
import base64
import io
import cv2
import numpy as np
from PIL import Image
import os

def qrck(img):
    img_out = Image.open(io.BytesIO(base64.b64decode(img)))
    img_out = np.array(img_out)
    S = Image.fromarray(img_out)
    S.save('./convert.png', 'png')
    a = Image.open("./convert.png")
    decoded = decode(a)
    os.remove("./convert.png")
    if len(decoded) == 1:
        for d in decoded:
            barcode_data = d.data.decode("utf-8")
        return barcode_data
    else:
        return 'error'
