import logging
import other

logging.basicConfig(level="DEBUG", filename="mylogs.log",
                    format="%(asctime)s | %(name)s  | %(levelname)s: %(message)s"
                    )

logger = logging.getLogger("image")
logger.setLevel("DEBUG")

def dowload_image():
    logger.debug("dowlaod")
    print("скачую")
    logger.info("скачався файл")
    other.test()
    print("файл скачався")

dowload_image()
#
# def calc(a, b):
#
#     c = a+b * 2
#     logging.debug(f"call function calc: {a} and {b} = {c}")
#     return c
#
#
# a = int(input("a:"))
# b = int(input("b:"))
# print(calc(a, b))
#
# try:
#     file = open("config.txt")
# except Exception as e:
#     logging.error("something wrong" + str(e))
#
#
# logging.info("просто інфомрація")