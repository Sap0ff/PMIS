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
