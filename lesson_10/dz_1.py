import sys
def season(month):
    if month in range(1, 3) or month == 12:
        return 'Winter'
    elif month in range(3, 6):
        return 'Spring'
    elif month in range(6, 9):
        return 'Summer'
    elif month in range(9, 12):
        return 'Autumn'
#Використовуємо інструкцію raise у разі введення номера місяця, що не входить в діапазон від 1 до 12
    else:
        raise ValueError('Номер місяця повинен бути від 1 до 12.')
#Додаємо обробку виключень, якщо введене значення не є числом, а також додаємо обробку всіх інших помилок,
#що можуть виникнути.
try:
    month = int(input('Введіть номер місяця: '))
    print(season(month))
except ValueError as ex:
    print('Ви ввели некоректний символ:', ex, file=sys.stderr)
except Exception as ex:
    print('Сталася помилка:', ex, file=sys.stderr)















