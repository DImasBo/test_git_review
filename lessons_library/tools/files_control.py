from config import PROJECT_NAME


FILE_NAME = "data.txt"
print(PROJECT_NAME)

def save_data(words):
    with open(f"../{FILE_NAME}", "w") as f:
        f.write(" ".join(words))


def read_data():
    with open(f"../{FILE_NAME}") as f:
        return f.read().split()
