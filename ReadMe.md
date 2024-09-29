# Задача №1: Загрузка на github через git bash.

Переход в указанный каталог

<img src="https://github.com/user-attachments/assets/3e45278e-f227-4c96-b072-87de56ae9b58">

Добавление файлов в индекс для отслеживания изменений и проверка

<img src="https://github.com/user-attachments/assets/26ec322b-f68f-43b4-af37-f69d797c10fd">

Запушим в git

![image (2)](https://github.com/user-attachments/assets/8bea887e-9302-40f8-8177-9f1db21353d7)


Создание тега

<img src="https://github.com/user-attachments/assets/a84b995d-b092-4df4-8c04-a76e045a9727">


# Описание кода Задание №2

13.	Написать функцию, генерирующую пароль от 8 до 32 символов, которая включает буквы, цифры и спец символы
```
import random
import string

def generate_random_password():
    """
    Функция генерирует случайный пароль длиной от 8 до 32 символов,
    который включает буквы, цифры и специальные символы.

    :return: Сгенерированный пароль
    """
    # Случайная длина пароля от 8 до 32
    length = random.randint(8, 32)

    # Все возможные символы для пароля
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерация пароля
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def print_password(password):
    """
    Функция выводит пароль на экран.

    :param password: Сгенерированный пароль
    """
    print(f"Сгенерированный пароль: {password}")

# Пример использования функций

if __name__ == "__main__":
    random_password = generate_random_password()
    print_password(random_password)
```

# Пример вывода

<img src="https://github.com/user-attachments/assets/55c7de47-2d67-4f12-9c40-f6e0b36eac6d">

# Описание кода Задание №3

Вывод в виде таблице предмета и даты всех экзаменов

# вывод даты всех экзаменов по предметам 

```
import json

# Загрузка списка студентов
with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Печатаем заголовок
print(f"{'Предмет'} {'Дата экзамена'}")

# Заполняем данные
for student in data['students']:
    for grade in student['grades']:
        print(f"{grade['subject']} {grade['exam_date']}")
```

<img src="https://github.com/user-attachments/assets/4fe24302-ff90-4fcf-9f1a-c4a03893d049">
