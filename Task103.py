import random
import string
def check_password_strength(password):
    if len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
        return True
    return False
def generate_password():
    while True:
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=random.randint(8, 12)))
        if check_password_strength(password):
            return password
if __name__ == "__main__":
    attempts = 0
    while True:
        attempts += 1
        password = generate_password()
        if check_password_strength(password):
            print(f"Надежный пароль: {password}")
            print(f"Количество попыток: {attempts}")
            break
