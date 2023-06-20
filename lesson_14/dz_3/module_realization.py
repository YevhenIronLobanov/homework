from class_Tree import Tree
import random

dat = []
for _ in range(25):
    dat.append(random.randint(0, 50))

# Створюємо екземпляр класу Tree, в якому кореневим вузлом буде перший елемент сгенерованого нами списку
tree = Tree(dat[0])

tree.add_elements(dat[1:])
tree.display()
min_element = tree.find_min()
max_element = tree.find_max()
print('Мінімальне значення бінарного дерева:', min_element)
print('Максимальне значення бінарного дерева:', max_element)

# Видалення випадкового елемента із списка
key_to_delete = random.choice (dat)
tree.delete(key_to_delete)

# Виведення зміненого дерева
print('Бінарне дерево після видалення елемента зі значенням: ', key_to_delete)
tree.display()



