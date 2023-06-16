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

#Графічний вивід бінарного дерева в консолі
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.val
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2









