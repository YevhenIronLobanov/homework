def test_function(a, b):
    multiplication = a*b
    division = a/b
    return multiplication, division
result_multiplication, result_division = test_function(10, 2)
print("Результат множення:", result_multiplication)
print("Результат ділення:", result_division)