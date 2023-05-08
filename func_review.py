import time


def decoretor(func):
    def wrapper():
        first_point = time.perf_counter()
        print("Час початку роботи функції = ", first_point)
        func()
        second_point = time.perf_counter()
        print("Час кінця роботи функції = ", second_point)
        print(f"Функція виконувалась  = {second_point - first_point:.8f} сек.")
    return wrapper

@decoretor
def hello():
    time.sleep(3)
    return("Hello, World!")

hello()
