import qrcode


with open('q.txt', 'r') as f:
    for i in f.readlines():
        word = str(i).strip('\n')

        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=2,
            border=3,
        )

        qr.add_data(f'https://rashanovin.com/profile/{word}')
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{word}.png")
