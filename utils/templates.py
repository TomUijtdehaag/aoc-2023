day_template = """from utils.read import readlines
                
def parse(input: list[str]):
    pass

def one(input):
    pass

def two(input):
    pass

if __name__ == "__main__":
    lines = readlines("input/{day}.txt")
    input = parse(lines)

    print("Part one:", one(input))
    print("Part two:", two(input))"""


test_template = """from d{day} import one, two, parse
                
test_input = ""

def test_parse():
    assert parse(test_input) == None


def test_one():
    assert one(test_input) == None


def test_two():
    assert two(test_input) == None """
