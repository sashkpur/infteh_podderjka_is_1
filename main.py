import random

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print(f"Числа: {a} и {b}")
    print(f"Сумма: {add(a, b)}")
    print(f"Произведение: {multiply(a, b)}")

if __name__ == "__main__":
    main()