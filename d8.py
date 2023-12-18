import math
from dataclasses import dataclass

from utils.read import readlines


@dataclass
class Node:
    name: str
    left: str
    right: str

    def __eq__(self, other):
        return self.name == other.name


@dataclass
class Graph:
    instructions: str
    nodes: dict[str, Node]

    def steps(self):
        current = "AAA"
        end = self.nodes["ZZZ"]

        s = 0
        while self.nodes[current] != end:
            instruction = self.instructions[s % len(self.instructions)]
            s += 1

            if instruction == "R":
                current = self.nodes[current].right
            elif instruction == "L":
                current = self.nodes[current].left

        return s

    def steps_two(self):
        currents = [name for name in self.nodes if name.endswith("A")]

        end_nodes = {}

        s = 0
        while len(end_nodes) < len(currents):
            instruction = self.instructions[s % len(self.instructions)]
            s += 1

            new_currents = []
            for i, current in enumerate(currents):
                if instruction == "R":
                    new_current = self.nodes[current].right
                elif instruction == "L":
                    new_current = self.nodes[current].left

                if new_current.endswith("Z"):
                    end_nodes[i] = s

                new_currents.append(new_current)

            currents = new_currents

        return math.lcm(*end_nodes.values())

    @classmethod
    def parse(cls, lines: list[str]):
        instructions, _, *nodes_str = lines

        nodes = {}

        for node in nodes_str:
            name, left_right = node.split(" = ")
            left, right = left_right.strip("()").split(", ")

            n = Node(name, left, right)
            nodes[name] = n

        return cls(instructions, nodes)


def one(graph: Graph):
    return graph.steps()


def two(graph: Graph):
    return graph.steps_two()


if __name__ == "__main__":
    lines = readlines("input/8.txt")
    graph = Graph.parse(lines)

    print("Part one:", one(graph))
    print("Part two:", two(graph))
