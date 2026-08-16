import ctypes
import os
import sys
from plyer import filechooser

from scan import read_qr_code
from generation import create_qr

def init_dpi_awareness() -> None:
    """Включает поддержку высокого разрешения (DPI) для четкости окон в Windows."""
    if sys.platform == "win32":
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass

def main() -> None:
    init_dpi_awareness()
    
    menu_text = (
        "\n🤖 Доступные опции:\n"
        "[1] Сгенерировать QR-код\n"
        "[2] Сканировать QR-код из файла\n"
        "[3] Выход\n"
    )
    
    while True:
        print(menu_text)
        choice = input('Выберите действие: ').strip()
        
        # Проверяем, что введено число
        if not choice.isdigit():
            print("⚠️ Пожалуйста, введите корректный номер пункта.")
            continue
            
        match int(choice):
            case 1:
                text = input('Введите текст или ссылку для QR-кода: ').strip()
                if not text:
                    print("⚠️ Текст не может быть пустым!")
                    continue
                try:
                    create_qr(text=text)
                except Exception as e:
                    print(f"❌ Ошибка при генерации: {e}")
                    
            case 2:
                print("⏳ Открытие проводника...")
                # filechooser.open_file возвращает список (или кортеж) путей
                paths = filechooser.open_file(
                    title="Выберите изображение QR-кода",
                    multiple=False,
                    filters=[("Изображения", "*.png", "*.jpg", "*.jpeg")]
                )
                
                if paths and paths[0]:
                    file_path = paths[0]
                    print(f'🔍 Выбран файл: {file_path}')
                    
                    if not os.path.exists(file_path):
                        print("⚠️ Файл больше не существует по указанному пути.")
                        continue
                        
                    try:
                        read_qr_code(file_path)
                    except Exception as e:
                        print(f"❌ Не удалось прочесть QR-код: {e}")
                else:
                    print("🚫 Выбор файла отменен.")
                    
            case 3:
                print("👋 Выход из программы.")
                break
                
            case _:
                print("⚠️ Неизвестная опция. Попробуйте снова.")

if __name__ == "__main__":
    main()
