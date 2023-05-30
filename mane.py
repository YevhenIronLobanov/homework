def mane_function(a, b):
    addition = a + b
    subtraction = a - b
    square = a**b
    return addition, subtraction, square
result_addition, result_subtraction, result_square = mane_function(10, 2)
print("Результат додавання:", result_addition)
print("Результат віднімання:", result_subtraction)
print("Зведення в ступінь:", result_square)
