# 🤖 Quick-Response-code

## 🚀 Основные возможности
- Генерация красивых QR-кодов (в форматах PNG, SVG, PDF) для быстрой делёжки ссылками.
- Сканирование QR-кодов

## 🛠️ Стек технологий
- **Язык:** Python 3.10+
- **Библиотеки:** `segno` + `Pillow` (генерация QR), `plyer` (выбор файлов), `colorama`.

## 💻 Инструкция по установке и запуску

### 1. Подготовка системы (Важно для QR)
Проект использует библиотеку `pyzbar`/`segno`. Для её корректной работы в системе должен быть установлен графический движок:
- **Windows:** Установите официальный пакет [ZBar](http://sourceforge.net).
- **Linux (Ubuntu/Debian):** `sudo apt-get install libzbar0`
- **macOS:** `brew install zbar`

### 2. Клонирование репозитория
```bash
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd Quick-Response-code
```

### 3. Настройка окружения и установка
Проект использует современный стандарт настройки `pyproject.toml`.

**Для Windows:**
```bash
# Создаем виртуальное окружение
python -m venv .venv

# Активируем его
.venv\Scripts\activate

# Устанавливаем проект и все его зависимости
pip install .
```

**Для Linux / macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install .
```

### 4. Настройка конфигурации
1. Создайте файл конфигурации (или укажите токен в коде).
2. Запустите бота:
```bash
python main.py
```