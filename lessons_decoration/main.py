import random
# def test(user):
#     msg = "Hi " + user
#
#     def sendMsg():
#         nonlocal msg
#         msg = "test"
#         print(msg)
#
#     sendMsg()
#     print(msg)
#
#
#
# test("Dmytro")

# def get_login(role):
#
#     def login():
#
#         print("login", role)
#
#     return login
#
# login_admin = get_login("Admin")
#
# get_login("Admin")()
#
# login_client = get_login("Client")
# login_manager = get_login("Manager")
# login_admin()


# def launchCounter():
#     counter = 0
#
#     def incrementCounter():
#         nonlocal counter
#         counter += 1
#         return counter
#
#     return incrementCounter
#
# n = launchCounter()
#
# n1 = n()
# print(n1)
#
#
# n2 = n()
# print(n2)
#
# n3 = n()
# print(n3)

#
# def test(func):
#     print("todo in test decorator!!!!")
#
#     def wrapper():
#         print("before")
#         func()
#         print("after")
#
#     return wrapper
#
#
# @test
# def print_user():
#     print("Hello Dmytro")
#
#
# print_user()
# from datetime import datetime
#
#
# def logger(func):
#     def wrapper():
#         print("=========before run function", func.__name__, datetime.now(), "===============")
#         func()
#     return wrapper
#
#
# @logger
# def login():
#     print("I am login")
#
# @logger
# def logout():
#     print("I am logout")
#
#
# login()
# logout()

#
# def dec(func):
#     def wrapper(a, b):
#         print(a,b, " аргументи для функці")
#         res = func(a, b)
#         return res
#     return wrapper
#
# @dec
# def dobutok(a, b):
#     return a*b
# a = dobutok(10, 5)
# print(a)
#
# from functools import wraps
#
#
# def counter_call(func):
#     @wraps(func)
#     def wrapper(word):
#         res = func(word)
#         wrapper.counter += 1
#         return res
#     wrapper.counter = 0
#     return wrapper
#
#users = []
# @counter_call
# def find_user(word):
#     print("я шукаю", word)
#     return word
#
# find_user("test")
# find_user("test2")
# find_user("test3")
# print(find_user.counter)
# find_user("test4")
#
# print(find_user.counter)
#
# import time
# from functools import lru_cache
#
#
# @lru_cache(maxsize=None)
# def fibonacci(n):
#     if n < 2:
#         return n
#     time.sleep(1)
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# start_time = time.perf_counter()
#
# print(fibonacci(5))
#
# end_time = time.perf_counter()
# print(f"The execution time: {end_time - start_time:.8f} seconds")
#
#
# start_time = time.perf_counter()
# print(fibonacci(5))
# end_time = time.perf_counter()
# print(f"The execution time: {end_time - start_time:.8f} seconds")

from functools import wraps
import time

def cache(func):
    @wraps(func)
    def wrapper(a):
        cache_key = a
        if cache_key in wrapper.cache:
            return wrapper.cache[cache_key]
        else:
            res = func(a)
            wrapper.cache[cache_key] = res
        return res

    wrapper.cache = {}
    return wrapper





# @cache
# def fibonacci(n):
#     if n < 2:
#         return n
#     time.sleep(1)
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci.cache)
#
# print(fibonacci(5))
# print(fibonacci.cache)
# print(fibonacci(5))
# print(fibonacci(5))


@cache
def download_image(PATH):
    time_download = random.randint(2, 5)
    time.sleep(time_download)
    print(time_download)
    return time_download


print(download_image("test.jpg"))
print(download_image("itstep.jpg"))
print("----------")
print(download_image("test.jpg"))

print(download_image.cache)