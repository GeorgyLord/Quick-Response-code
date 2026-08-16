import os
from PIL import Image
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # 1. Проверяем, существует ли файл
    if not os.path.exists(image_path):
        print(f"Ошибка: Файл '{image_path}' не найден.")
        return

    try:
        # 2. Открываем изображение
        img = Image.open(image_path)
        
        # 3. Убираем прозрачность (альфа-канал), заменяя её на белый фон
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            background = Image.new("RGB", img.size, (255, 255, 255))
            # Используем последний канал (альфа) как маску для наложения
            background.paste(img, mask=img.split()[-1])
            img = background
        else:
            img = img.convert("RGB")

        # 4. Первая попытка распознавания в оригинальном размере
        result = decode(img)

        # 5. Вторая попытка: если не распозналось, оптимизируем размер (делаем 600x600)
        if not result:
            img_resized = img.resize((600, 600), Image.Resampling.LANCZOS)
            result = decode(img_resized)

        # 6. Вывод результатов
        if not result:
            print("Библиотека pyzbar не смогла считать этот QR-код.")
            print("Возможно, в системе не установлен системный пакет zbar.")
        else:
            print(f"Успешно найдено QR-кодов: {len(result)}\n")
            for index, obj in enumerate(result, 1):
                print(f"--- QR-код №{index} ---")
                print("Тип:", obj.type)
                print("Данные:", obj.data.decode("utf-8"))
                
    except Exception as e:
        print(f"Произошла непредвиденная ошибка при обработке файла: {e}")

# Запуск программы для вашего файла
if __name__ == "__main__":
    read_qr_code("custom_qr.png")
