def generate_greeting(name: str) -> str:
    """
    Функция для генерации приветственного сообщения.

    Args:
        name (str): Имя человека.

    Returns:
        str: Приветственное сообщение.
    """
    return f"Привет, {name}! Добро пожаловать в наш проект."


# Точка входа в программу
if __name__ == "__main__":
    name = input("Введите ваше имя: ")
    print(generate_greeting(name))