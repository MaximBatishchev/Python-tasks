def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = int(input("Введите число: "))
    if isPrime(number):
        print(f"{number} является простым числом.")
    else:
        print(f"{number} не является простым числом.")
