"""Напишите функцию, которая проверяет,
является ли данная строка палиндромом или нет,
и возвращает результат проверки. Пример:
check_palindrome("test")  # False
check_palindrome("Кит на море не романтик")  # True
"""


# Решение

def check_palindrome(text):
    text = text.lower()
    text = text.replace(" ", "")
    text_b = text[::-1]

    if text == text_b:
        return True
    else:
        return False


print(check_palindrome("Кит на море не романтик"))
