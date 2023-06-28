import random
import sys
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
    def create_matrix(self, a, b):
        '''Метод наповнення матриці числами'''
        matrix = [[random.randint(a, b) for _ in range(self.columns)] for _ in range(self.rows)]
        return matrix
    def plus_minus_matrix(self, matrix_1, matrix_2):
        '''Метод додавання та віднімання матриць'''
        # У разі неспіврозмірності матриць приводимо матриці до співрозмірності доповнючи матрицю "0"
        if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
            rw = max(len(matrix_1), len(matrix_2))
            col = max(len(matrix_1[0]), len(matrix_2[0]))
            new_matrix_1 = [[0] * col for _ in range(rw)]
            new_matrix_2 = [[0] * col for _ in range(rw)]
            for i in range(len(matrix_1)):
                for j in range(len(matrix_1[0])):
                    new_matrix_1[i][j] = matrix_1[i][j]
            for i in range(len(matrix_2)):
                for j in range(len(matrix_2[0])):
                    new_matrix_2[i][j] = matrix_2[i][j]
            matrix_1 = new_matrix_1
            matrix_2 = new_matrix_2

        result_plus = []
        result_minus = []
        for i in range(self.rows):
            row_plus = []
            row_minus = []
            for j in range(self.columns):
                row_plus.append(matrix_1[i][j] + matrix_2[i][j])
                row_minus.append(matrix_1[i][j] - matrix_2[i][j])
            result_plus.append(row_plus)
            result_minus.append(row_minus)
        return result_plus, result_minus
    def constant_matrix(self, const, matrix):
        ''' Метод множення на константу'''
        results_const = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(const * matrix[i][j])
            results_const.append(row)
        return results_const
    def mult_matrix(self, matrix_1, matrix_2):
        '''Метод множення матриць'''
        try:
            if len(matrix_1[0]) != len(matrix_2):
                raise ValueError('Неспіврозмірність матриць')

            results_mult = []
            for i in range(len(matrix_1)):
                row = []
                for j in range(len(matrix_2[0])):
                    sum_val = 0
                    for k in range(len(matrix_2)):
                        sum_val += matrix_1[i][k] * matrix_2[k][j]
                    row.append(sum_val)
                results_mult.append(row)
            return results_mult
        except ValueError as ex:
            print('Помилка:', ex, file=sys.stderr)
    def trans_matrix(self, matrix):
        '''Метод транспонування матриці'''
        result_trans = []
        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(matrix[j][i])
            result_trans.append(row)
        return result_trans

#Приклади застосування
#Cтворення матриць
instant_matrix = Matrix (3, 3)
A = instant_matrix.create_matrix(1, 50)
print('Матриця А:')
for r in A:
    print(r)
B = instant_matrix.create_matrix(1, 50)
print('Матриця B:')
for r in B:
    print(r)
#Додавання та віднімання матриць
result_plus, result_minus = instant_matrix.plus_minus_matrix(A, B)
print('Результат додавання:')
for r in result_plus:
    print(r)
print('Результат віднімання:')
for r in result_minus:
    print(r)
#Множення матриці на константу
results_const = instant_matrix.constant_matrix(5,A)
print('Результат множення матриці на константу:')
for r in results_const:
    print(r)
#Множення матриць між собою
results_mult = instant_matrix.mult_matrix(A, B)
print('Результат множення матриці на матрицю:')
for r in results_mult:
    print(r)
#Транспонування матриць
result_trans = instant_matrix.trans_matrix(A)
print('Результат транспонування матриці: ')
for r in result_trans:
    print(r)


























