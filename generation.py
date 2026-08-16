import re
from datetime import datetime
from pathlib import Path
import segno

def slugify(text: str, max_length: int = 20) -> str:
    """Создает безопасное имя файла из введенного текста."""
    # Удаляем спецсимволы, заменяем пробелы на дефисы
    slug = re.sub(r'[^\w\s-]', '', text.lower())
    slug = re.sub(r'[\s_]+', '-', slug).strip()
    return slug[:max_length] if slug else "qrcode"

def create_qr(text: str) -> None:
    """Генерирует QR-код с максимальной избыточностью во множестве форматов."""
    # Создаем объект кода
    qr = segno.make_qr(text, error="H")

    # Конфигурация стильного дизайна
    design_kwargs = {
        "scale": 10,                 # Пропорции размера
        "border": 4,                 # Поля вокруг кода
        "dark": "#1a1a2e",           # Цвет модулей (темно-синий)
        "light": "#ffffff",          # Цвет фона (белый)
    }

    # Инициализируем директорию для экспорта
    output_dir = Path("qr_exports")
    output_dir.mkdir(exist_ok=True)

    # Формируем уникальное имя файла (текст_дата_время)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_text = slugify(text)
    filename_base = f"{safe_text}_{timestamp}"

    # Словарь расширений для автоматического сохранения в цикле
    # Это избавляет код от дублирования строк qr.save(...)
    formats = [".svg", ".eps", ".png", ".pdf"]

    print("⚙️ Начало генерации файлов...")
    for ext in formats:
        full_path = output_dir / f"{filename_base}{ext}"
        qr.save(full_path, **design_kwargs)
        print(f"✅ Создан: {full_path}")

    print(f"\n🎉 Все форматы успешно сгенерированы в папке '{output_dir}'!")
