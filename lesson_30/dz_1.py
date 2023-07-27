class HashTable:
    def __init__(self, size):
        self.size = size
        # Визначаємо None, як пусту комірку та встановлюємо лічильник щодо кількості елементів в хеш-таблиці
        self.hash_table = [None] * size
        self.__ful = 0
        '''Конструктор класу який ініціює об'єкт хеш-таблиці'''
    #Реалізуємо функцію хешуванння
    def _hash_function(self, key):
        return key % self.size

    def insert_data(self, key, data):
        '''Метод вставки елементів'''
        hash_value = self._hash_function(key)
        index = hash_value
        # Пошук пустої чи видаленої комірки
        while self.hash_table[index] is not None and self.hash_table[index][0] is not None:
            if self.hash_table[index][0] == key:
                # Якщо ключ вже є, оновлюємо значення
                self.hash_table[index][1] = data
                return
            index += 1
            if index >= self.size:
                index = 0

        # Вставка елемента
        self.hash_table[index] = [key, data]
        self.__ful += 1
    def search_data(self, key):
        '''Метод пошуку даних по ключу'''
        hash_value = self._hash_function(key)
        index = hash_value

        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                # Повертаємо значення, якщо ключ знайдений, якщо ні повертаємо None
                return self.hash_table[index][1]
            index += 1
            if index >= self.size:
                index = 0
        return None
    def remove_data(self, key):
        '''Метод видалення елемента'''
        hash_value = self._hash_function(key)
        index = hash_value

        while self.hash_table[index] is not None:
            if self.hash_table[index][0] == key:
                # Відмічаємо ключ видаленним і зменшуєм лічільник
                self.hash_table[index][0] = None
                self.__ful -= 1
                return
            index += 1
            if index >= self.size:
                index = 0
    def __str__(self):
        '''Метод представлення хеш-таблиці у вигляді рядка'''
        return str(self.hash_table)

# Приклад використання
hash_table = HashTable(10)
hash_table.insert_data(1, 'BMW')
hash_table.insert_data(2, 'Opel')
hash_table.insert_data(4, 'Audi')
hash_table.insert_data(9, 'Toyota')
hash_table.insert_data(12, 'Mercedes')

print(hash_table.search_data(9))
print(hash_table.search_data(4))

hash_table.remove_data(2)
print(hash_table.search_data(2))

print(hash_table)