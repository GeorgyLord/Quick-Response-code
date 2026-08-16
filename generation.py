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


# import qrcode

# qr = qrcode.QRCode(
#     version=1,  # Размер матрицы (от 1 до 40)
#     error_correction=qrcode.constants.ERROR_CORRECT_H,  # Высокий уровень стойкости к повреждениям
#     box_size=1,  # Количество пикселей на одну точку
#     border=4,  # Толщина рамки (рекоммендуемо 4)
# )

# qr.add_data("https://github.com")
# qr.make(fit=True)

# # Изменение цвета кода и фона
# img = qr.make_image(fill_color="black", back_color="white")
# img.save("custom_qr.png")




from pathlib import Path
import segno

# 1. Создаем объект QR-кода с максимальным уровнем избыточности 'H'
# Уровень 'H' (High) позволяет восстановить до 30% поврежденного или перекрытого кода
# "L", "M", "Q", "H"
def create_qr(text):
    qr = segno.make_qr(text, error="H")

    # Настройки дизайна
    design_kwargs = {
        "scale": 10,                 # Размер
        "border": 4,                 # Ширина белой рамки
        "dark": "#1a1a2e",           # Цвет основных модулей (темно-синий)
        "light": "#ffffff",          # Цвет фона (белый)
    }


    # Папка для сохранения результатов
    output_dir = Path("qr_exports")
    output_dir.mkdir(exist_ok=True)

    # SVG (Широко используется в веб-дизайне)
    qr.save(output_dir / "crypto_bot.svg", **design_kwargs)

    # EPS (Стандарт для типографий и Adobe Illustrator)
    qr.save(output_dir / "crypto_bot.eps", **design_kwargs)


    # PNG (Идеально для веба и мессенджеров, поддерживает прозрачность)
    # Чтобы сделать фон прозрачным, замените в design_kwargs: "light": None
    qr.save(output_dir / "crypto_bot.png", **design_kwargs)

    # PDF (Удобно для отправки документов или инструкций)
    qr.save(output_dir / "crypto_bot.pdf", **design_kwargs)

    print("Все форматы успешно сгенерированы в папке qr_exports!")
