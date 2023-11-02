from pyzbar.pyzbar import decode
import base64
import io
import cv2
import numpy as np
from PIL import Image
import os
import zbar

def qrck(img):
    img_out = Image.open(io.BytesIO(base64.b64decode(img)))
    img_out = np.array(img_out)
    S = Image.fromarray(img_out)
    S.save('./convert.png', 'png')
    a = cv2.imread('./convert.png', cv2.IMREAD_GRAYSCALE)
    qrcode_data = ""
    scanner = zbar.Scanner()
    results = scanner.scan(a)
    for result in results:
        qrcode_data = result.data
    os.remove("./convert.png")
    if(qrcode_data=="null"):
        print("QR Code not detected")
        return 'error'
    else:
    # QR 코드가 인식이 되었다면
    # 인식된 QR 코드의 데이터를 출력해준다
        print(qrcode_data)
        return qrcode_data
