while True:
    print('Доступные опции:\n[1] Генерацию Qr-code\n[2] Сканирование Qr-code\n[3] Exit\n')
    text = input('Выберете: ').strip()
    try:
        text = int(text)
    except:
        continue
    if text == 1:
        pass
    elif text == 2:
        pass
    elif text == 3:
        break