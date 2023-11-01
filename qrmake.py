import qrcode

qr_bus = qrcode.QRCode(
    version = 4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=15,
    border=4,
)
qr_bus.add_data('precycler_bus')
qr_bus.make(fit=True)

img = qr_bus.make_image(fill_color="black", back_color="white")
img.save("./qr_bus.png")

qr_ecoact = qrcode.QRCode(
    version = 4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=15,
    border=4,
)
qr_ecoact.add_data('precycler_ecoact')
qr_ecoact.make(fit=True)

img = qr_ecoact.make_image(fill_color="black", back_color="white")
img.save("./qr_ecoact.png")

qr_use = qrcode.QRCode(
    version = 3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr_use.add_data('precycler_use_1000')
qr_use.make(fit=True)

img = qr_use.make_image(fill_color="black", back_color="white")
img.save("./qr_use.png")
