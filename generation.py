# import segno

# qrcode = segno.make_qr("Hello METANIT.COM")
# qrcode.save("metanit_qr.png", dark="#FF0000", border=4, scale=50)
# qrcode.show()


# from segno import helpers
 
# qrcode = helpers.make_wifi(ssid="MyWifi", password="1234567890", security="WPA")
# qrcode.save("wifi-access.png", scale=10)

# import io
# import qrcode

# qr = qrcode.QRCode()
# qr.add_data("https://docs-python.ru/packages/generator-qr-kodov/")
# f = io.StringIO()
# qr.print_ascii(out=f)
# f.seek(0)
# print(f.read())


import qrcode

qr = qrcode.QRCode(
    version=1,  # Размер матрицы (от 1 до 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Высокий уровень стойкости к повреждениям
    box_size=1,  # Количество пикселей на одну точку
    border=4,  # Толщина рамки (рекоммендуемо 4)
)

qr.add_data("https://github.com")
qr.make(fit=True)

# Изменение цвета кода и фона
img = qr.make_image(fill_color="black", back_color="white")
img.save("custom_qr.png")
