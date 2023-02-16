import random


def generate_random(num1, num2):
    while True:
        yield random.randint(num1, num2)


g1 = generate_random(10, 20)
print(next(g1))
print(next(g1))
