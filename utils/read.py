def read(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def readlines(path: str) -> str:
    with open(path, "r") as f:
        lines = f.readlines()
        return [line.strip("\n") for line in lines]
