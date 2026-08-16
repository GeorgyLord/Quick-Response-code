import ctypes
from plyer import filechooser

from scan import read_qr_code
from generation import create_qr


try:
    # Метод для Windows 8.1 / 10 / 11 (динамическое масштабирование под монитор)
    ctypes.windll.shcore.SetProcessDpiAwareness(2)  # 2 = PROCESS_PER_MONITOR_DPI_AWARE
except Exception:
    try:
        # Резервный метод для старых версий Windows 7 / 8
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


menu_text = '\nДоступные опции:\n[1] Генерацию Qr-code\n[2] Сканирование Qr-code\n[3] Exit\n'
while True:
    print(menu_text)
    number_option = input('Выберете: ').strip()
    try:
        number_option = int(number_option)
    except:
        continue
    if number_option == 1:
        text = input('Введите текст qr-кода: ')
        create_qr(text=text)
    elif number_option == 2:
        path = filechooser.open_file(
            title="Выберите файл для бота",
            multiple=False,  # True, если нужно выбрать несколько
            filters=[("Изображения и конфиги", "*.png", "*.jpg", "*.toml")]
        )
        if path:
            print('Выбрано изображение:', path)
            read_qr_code(path[0])
        pass
    elif number_option == 3:
        break
