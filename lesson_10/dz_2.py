import sys
def unique_numbers(numbers):
    try:
        if len(numbers) == len(set(numbers)):
            print('Всі числа унікальні.')
        else:
            print('Є числа, що повторюються.')
    except TypeError as ex:
        print('Некоректно введені дані. Перевірте список на наявність тільки чисел.', ex, file=sys.stderr)
    except ValueError as ex:
        print('Некоректні дані. Перевірте чи всі елементи є числами.', ex, file=sys.stderr)

input_list = input('Введіть через пробіл числа: ').split()
try:
    numbers = list(map(int, input_list))
    if len(numbers) == 0:
        raise ValueError('Список чисел порожній.')
    unique_numbers(numbers)
except ValueError as ex:
    print('Некоректні дані.', ex, file=sys.stderr)
except Exception as ex:
    print('Сталася помилка.', ex, file=sys.stderr)

