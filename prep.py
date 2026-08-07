from asyncio import sleep

import time
def number(*arg):
    for i in arg:
        print(i)




number(1, 2, 3, 4, 5)


def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])



student(name ="Jon" , age= 2333)



def login():
    print(("User logged in"))


def wrapper():
    print("Please wait for login...")
    time.sleep(1)

    login()
    print("User logged in successfully")

wrapper()


print(__name__)

def demo():
    return 10
