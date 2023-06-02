class Parallelogram:
    def __init__(self, width, length):
        """Ініціалізація атрибутів"""
        self.width = width
        self.length = length
    def get_area(self):
        """Розрахунок площи паралелограма"""
        return self.width * self.length
class Square(Parallelogram):
    def __init__(self, side_length):
        """Инициализуємо атрибут сторони"""
#Викликаємо конструктор батьківського класу
        super().__init__(side_length, side_length)
    def get_area(self):
        """Розраховуємо площу квадрата"""
        return self.length ** 2

#Створюємо екземпляри і виводимо результат в консоль
pr = Parallelogram(25, 10)
sq = Square(30)
print('Площа паралелограма:', pr.get_area())
print('Площа квадрата:', sq.get_area())

