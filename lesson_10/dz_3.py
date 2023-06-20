import sys
class CustomIntFloatValueError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Невірний тип числа "{self.value}". Як значення можуть бути прийняті лише цілі числа.'
try:
    raise CustomIntFloatValueError(5.17)
except CustomIntFloatValueError as er:
    print(er, file=sys.stderr)