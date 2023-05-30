def mane_function(a, b):
    plus = (a + b)*a
    minus = (a - b)*b
    cub = (a**b)
    return plus, minus, cub
result_plus, result_minus, result_cub = mane_function(10, 3)
print("Результат з додаванням:", result_plus)
print("Результат з відніманням:", result_minus)
print("Зведення в куб:", result_cub)

