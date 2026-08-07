import time

numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)
    # time.sleep(3)


def demo():
    return 100


print(demo())


def hello():
    yield 13
    print("Hello")

print(next(hello()))
