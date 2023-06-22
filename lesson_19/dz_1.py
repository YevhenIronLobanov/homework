import csv
import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
g = nx.Graph()

# Створюємо порожній список, який буде містити інформацію про міста та відстані між ними
cities = []

# Відкриваємо файл cities.csv в режимі читання та зчитуємо інформацію з файлу.
with open('cities.csv', 'r') as filecsv:
    reader = csv.reader(filecsv, delimiter=';')

    # За допомогою циклу проходимо по змінній reader та додаємо інформацію до створеного порожнього списку
    for element in reader:
        cities.append([element[0], element[1], int(element[2])])


        # Додаємо вершини та ребра до графа
        g.add_edge(element[0], element[1], weight=int(element[2]))

# Створюємо позиції вершин для візуалізації графа звикористанням spring_layout
position = nx.spring_layout(g, seed=42)

# Візуалізація графа
plt.figure(figsize=(50, 100))
nx.draw_networkx(g, position, node_size=50)

# Відображення графа
plt.title('Міста України')
plt.axis('off')
plt.tight_layout(w_pad=None, h_pad=None, rect=None)
plt.show()