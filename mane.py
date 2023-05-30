def mane_function(a, b):
    addition = a + b
    subtraction = a - b
    square = a**b
    return addition, subtraction, square
result_addition, result_subtraction, result_square = mane_function(10, 2)



def test_function(a, b):
    multiplication = a*b
    division = a/b
    return multiplication, division


result_multiplication, result_division = test_function(10, 2)
print("Результат множення:", result_multiplication)
print("Результат ділення:", result_division)