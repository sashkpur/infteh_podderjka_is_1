from calculator import add, multiply, minus, generate_random_pair

def main():
    a, b = generate_random_pair()
    print(f"Числа: {a} и {b}")
    print(f"Сумма: {add(a, b)}")
    print(f"Произведение: {multiply(a, b)}")
    print(f"Разность: {minus(a, b)}")

if __name__ == "__main__":
    main()
