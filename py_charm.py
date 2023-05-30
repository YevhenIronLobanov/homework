def mane_function(a, b):
    plus = (a + b)*a
    minus = (a - b)*b
    cub = (a**b)
    return plus, minus, cub
result_plus, result_minus, result_cub = mane_function(10, 3)
print("Результат з додаванням:", result_plus)
print("Результат з відніманням:", result_minus)
print("Зведення в куб:", result_cub)

def test_function(a, b):
    multiplication = a*b
    division = a/b
    return multiplication, division
result_multiplication, result_division = test_function(10, 2)
print("Результат множення:", result_multiplication)
print("Результат ділення:", result_division)