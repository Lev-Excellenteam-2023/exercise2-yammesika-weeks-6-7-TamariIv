import time


def timer(f, *args, **kwargs):
    start, finish = 0, 0
    if args:
        start = time.time()
        f(*args)
        finish = time.time()
    elif kwargs:
        start = time.time()
        f(**kwargs)
        finish = time.time()
    return finish - start


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
