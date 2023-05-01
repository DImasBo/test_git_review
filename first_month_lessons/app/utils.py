
def calc(m, *args, operation="*"):
    if operation == "*":
        r = 1
        for i in args:
            r *= i
        return r

    if operation == "+":
        r = 1
        for i in args:
            r += i
        return r


def print_list(l):
    return
