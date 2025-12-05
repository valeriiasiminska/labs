from decorator import delay   # Імпортуємо декоратор з окремого файлу

@delay(4)   # Додаємо 4 секунди затримки перед поверненням результату
def show_quote():
    """
    Повертає цитату після виконання та затримки.
    """
    print("Виводжу цитату...")
    return "Hello World"

def main():
    print("Початок роботи...")
    result = show_quote()       # Виклик функції з декоратором
    print("Результат повернувся:")
    print(result)

if __name__ == "__main__":
    main()
