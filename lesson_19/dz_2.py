import csv
import networkx as nx
import sys
#Створюємо порожній список, який містить інформацію про міста і відстань між ними
cities = []
# Відкриваємо файл cities.csv в режимі читання і зчитуємо инфу з файла.
with open('cities.csv', 'r') as filecsv:
    reader = csv.reader(filecsv, delimiter=';')
# За допомогою цикла проходимо по змінній  reader і додаємо інфу в створений список
    for element in reader:
        cities.append([element[0], element[1], int(element[2])])
#Cтворюємо екземпляр класу networkx и додаємо міста і ребра з відстанями в граф
g = nx.Graph()
for edge in cities:
    g.add_edge(edge[0], edge[1], weight=edge[2])

#Створюємо функцію яка приймає назву міст і виводить значення маршруту та протяжність шляху
def ukr_citi():
    print('Введіть назву міста (латинськими літерами):')
    start_citi = input('- відправлення: ')
    end_citi = input('- прибуття: ')
    ##Додаємо обробку помилок, якщо одне з введених міст або обидва відсутні у списку
    try:
        route = nx.shortest_path(g, start_citi, end_citi, weight='weight')
        distance = nx.shortest_path_length(g, start_citi, end_citi, weight='weight')
        print('Маршрут шляху: ', route)
        print('Протяжність шляху: ', distance, 'km')
    except nx.NodeNotFound as ex:
        print('Введене місто (міста) відсутні в каталозі.', ex, file= sys.stderr)
ukr_citi()