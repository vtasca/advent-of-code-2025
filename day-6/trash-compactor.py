from pathlib import Path
import math
PUZZLE_INPUT_PATH = Path("day-6/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def calculate_sum_of_components(puzzle_input: str) -> int:
    rows = [y.split() for y in[x for x in puzzle_input.split('\n')]]

    cols = len(rows[0])

    operations = []
    operation_list = []
    for col in range(cols):
        for row in range(len(rows)):
            operations.append(rows[row][col])
        operation_list.append(operations)
        operations = []

    components = []
    for op_list in operation_list:
        if op_list[-1] == '+':
            sum_of_numbers = sum(int(x) for x in op_list[:-1])
            components.append(sum_of_numbers)
            # print(sum_of_numbers)
        elif op_list[-1] == '*':
            product_of_numbers = math.prod(int(x) for x in op_list[:-1])
            components.append(product_of_numbers)
            # print(product_of_numbers)

    return sum(components)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)
    
    print(calculate_sum_of_components(puzzle_input))