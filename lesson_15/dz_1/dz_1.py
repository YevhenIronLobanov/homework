# -*- coding: utf-8 -*-
import  socket
import logging

# Визначаємо конфігурацію логгера
logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Створюємо додаткові обробники для додаткових рівней WARNING та ERROR
warning_handler = logging.FileHandler('server.log')
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

error_handler = logging.FileHandler('server.log')
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Доаємо обробник до головного логгера
root_logger = logging.getLogger('')
root_logger.addHandler(warning_handler)
root_logger.addHandler(error_handler)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
logging.info('Запущено роботу сервера (для зупинки роботи сервера натисніть Ctrl+C)')

while True:
    conn, addr = sock.accept()
    logging.info('Підключено: %s', addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        received_message = data.decode('UTF-8')
        logging.info('Клієнт: %s', received_message)

        if received_message == 'Клієнт припинив роботу.':
            break

        answer = input('Сервер: ')
        logging.info('Сервер: %s', answer)
        conn.send(bytes(answer, encoding='UTF-8'))

    conn.close()