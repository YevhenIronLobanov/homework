class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#Метод додавання елемента зі списка та порядок формування бінарного дерева
    def add_elements(self, elements):
        for element in elements:
            self.insert(element)
    def insert(self, key):
        if key < self.val:
            if self.left:
                self.left.insert(key)
            else:
                self.left = Tree(key)
                return
        else:
            if self.right:
                self.right.insert(key)
            else:
                self.right = Tree(key)
                return
#Пошук мінімального елемента
    def find_min(self):
        root = self
        while root.left:
            root = root.left
        return root.val
#Пошук максимального елемента
    def find_max(self):
        root = self
        while root.right:
            root= root.right
        return root.val
#Метод видалення елемента
    def delete(self, key):
        if key < self.val:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.val:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                min_right_subtr = self.right.find_min()
                self.val = min_right_subtr
                self.right = self.right.delete(min_right_subtr)
        return self