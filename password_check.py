import hashlib


def check_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True

    if not has_upper or not has_lower:
        return False

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    if not has_digit:
        return False

    return True


def main():
    password = input("Введите пароль: ")

    if check_password(password):
        print("Пароль достаточно сложный.")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(f"Хеш-значение пароля: {hashed_password}")
    else:
        print("Пароль не соответствует требованиям.")


if __name__ == "__main__":
    main()
