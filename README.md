# создаем виртуальное окружение, если нет
python -m venv .venv

# активируем виртуальное окружение
source .venv/Scripts/activate

# Установка необходимых библиотек
pip install -r requirements.txt

pip install .