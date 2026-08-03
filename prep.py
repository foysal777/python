def number(*arg):
    for i in arg:
        print(i)




number(1, 2, 3, 4, 5)


def student(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])



student(name ="Jon" , age= 2333)

