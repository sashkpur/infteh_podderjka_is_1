import random

def add(a, b):
    return a + b

def multiply(a, b):
    return a - b

def minus(a, b):
    return a - b

def generate_random_pair(low=1, high=100):
    return random.randint(low, high), random.randint(low, high)