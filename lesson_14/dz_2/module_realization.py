from class_Tree import Tree
import random

dat = []
for _ in range(50):
    dat.append(random.randint(0, 100))

# Створюємо екземпляр класу Tree, в якому кореневим вузлом буде перший елемент сгенерованого нами списку
tree = Tree(dat[0])

tree.add_elements(dat[1:])
tree.display()
b = Tree.find_min(tree)
c = Tree.find_max(tree)
print('Мінімальне значення бінарного дерева:', b)
print('Максимальне значення бінарного дерева:', c)


