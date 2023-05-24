import logging


logging.basicConfig(level="DEBUG", filename="mylogs.log",
                    format="%(asctime)s | %(levelname)s: %(message)s"
                    )


def calc(a, b):

    c = a+b * 2
    logging.debug(f"call function calc: {a} and {b} = {c}")
    return c


a = int(input("a:"))
b = int(input("b:"))
print(calc(a, b))

try:
    file = open("config.txt")
except Exception as e:
    logging.error("something wrong" + str(e))

