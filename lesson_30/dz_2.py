import hashlib
# Створюємо порожній словник в якому будуть зберігатись логіни і хеші зареєстрованих користувачів
login_password_dict = {}

# Функція для хешування пароля
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Створюємо функцію яка додає логін і хешований пароль у словник
def add_login_password(login, password):
    hashed_password = hash_password(password)
    login_password_dict[login] = hashed_password


# Cтворення циклу для реєстрації користувача
while True:
    login = input('Введіть ваш логін (або "q" для виходу): ')
    if login.lower() == 'q':
        break

    password = input('Введіть ваш пароль: ')
    add_login_password(login, password)

print('Словник логін: хеш-пароль:')
print(login_password_dict)

#Створюємо функцію авторизації користувача
def authorize_user(login, password):
    if login in login_password_dict:
        hashed_password = hash_password(password)
        if hashed_password == login_password_dict[login]:
            return True
    return False
login_authorize = input('Введіть ваш логін для авторизації: ')
password_authorize = input('Введіть ваш пароль: ')

if authorize_user(login_authorize, password_authorize):
    print('Вітаємо! Авторизація успішна!')
else:
    print('Помилка авторизації. Ви ввели невірний логін або пароль.')