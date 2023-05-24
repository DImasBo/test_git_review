

# try:
#     a = open("test", "w")
#
#     a.write("test")
#
#     b = 5 / 0
#
#     a.write(b)
# except Exception as e:
#     print("error")
# finally:
#     a.close()
#
# with open("test", "w") as a:
#     a.write("test")

from contextlib import contextmanager


@contextmanager
def my_open(name_file, mode):
    try:
        # file = open(name_file, mode)
        a = "test my str"
        yield a
    except FileNotFoundError:
        print("warring file not found")
    finally:
        pass
        # file.close()


with my_open("test0.txt", "r") as f:
    print(f)
