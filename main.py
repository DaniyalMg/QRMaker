import qrcode

word = input('Enter a paragraph: ')

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=3,
)

qr.add_data(f'{word}')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{word}.png")
