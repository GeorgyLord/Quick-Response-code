from pathlib import Path
from typing import Final
from PIL import Image
from pyzbar.pyzbar import decode, Decoded

# Константа для целевого размера при оптимизации
OPTIMIZED_SIZE: Final[int] = 600

def read_qr_code(image_path: str | Path) -> None:
    """Открывает изображение, оптимизирует его для pyzbar и считывает данные из QR-кода."""
    # Конвертируем путь в объект Path для удобной работы
    path = Path(image_path)

    # 1. Проверка существования файла
    if not path.is_file():
        print(f"❌ Ошибка: Файл '{path.resolve()}' не найден или является папкой.")
        return

    try:
        # 2. Открываем изображение
        img = Image.open(path)
        
        # 3. Безопасное удаление прозрачности (альфа-канала)
        # Если в изображении есть прозрачность, накладываем его на чистый белый фон
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            background = Image.new("RGB", img.size, (255, 255, 255))
            # Забираем маску прозрачности (последний канал)
            alpha_mask = img.convert("RGBA").split()[-1]
            background.paste(img, mask=alpha_mask)
            img = background
        else:
            img = img.convert("RGB")

        # 4. Первая попытка распознавания (оригинальный размер)
        result: list[Decoded] = decode(img)

        # 5. Вторая попытка: оптимизация размера при неудаче
        if not result:
            img_resized = img.resize((OPTIMIZED_SIZE, OPTIMIZED_SIZE), Image.Resampling.LANCZOS)
            result = decode(img_resized)

        # 6. Вывод результатов
        if not result:
            print("⚠️ Не удалось считать QR-код.")
            print("💡 Убедитесь, что код не смазан, а в системе установлен пакет zbar (libzbar0 / brew install zbar).")
            return

        print(f"✅ Успешно найдено QR-кодов: {len(result)}\n")
        
        for index, obj in enumerate(result, 1):
            # Декодируем байты в строку, игнорируя возможные ошибки кодировки
            try:
                decoded_data = obj.data.decode("utf-8")
            except UnicodeDecodeError:
                decoded_data = obj.data.decode("utf-8", errors="replace")

            print(f"--- 📱 QR-код №{index} ---")
            print(f"Тип:    {obj.type}")
            print(f"Данные: {decoded_data}")
            print("-" * 22)
                
    except Exception as e:
        print(f"❌ Произошла непредвиденная ошибка при обработке файла: {e}")
