#import os, qrcode
import qrcode
from PIL import Image


face = Image.open('data/src/kusa.png')
face = face.resize((int(face.width / 2), int(face.height / 2)))

qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_M
)
qr_big.add_data('（　＾ω＾）＜Life Is a Joke.\n Thx!')
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')

pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('data/dst/qrcode.png')
