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

    print(puzzle_input)

    puzzle_list = [x for x in puzzle_input.split('\n')]
    puzzle_lists = [list(x) for x in puzzle_list]
    
    # print(puzzle_lists)

    # traverse matrix column-first
    puzzle_matrix = []
    numbers = []
    operations = []

    total = 0
    checkpoint = 0
    for i in range(len(puzzle_lists[0]), 0, -1):
        puzzle_rows = []
        number_in_progress = ''
        operation = ''
        size = 0
        for j in range(len(puzzle_lists)):
            point = puzzle_lists[j][i-1]
            puzzle_rows.append(point)
            if point != ' ' and point not in ['+', '*']:
                number_in_progress += point
            if point in ['+', '*']:
                operation = point
        
        if number_in_progress != '':
            numbers.append(number_in_progress)

        if operation != '':
            print(f"I: {i}")
            print(f"Checkpoint: {checkpoint}")

            if checkpoint == 0:
                size = len(puzzle_lists[0]) - i + 1
            else:
                size = - (i - checkpoint) - 1
            print(f"size: {size}")
            checkpoint = i
            operations.append(operation)
            if operation == '+':
                print(f"Adding {numbers[-size:]}: {sum(int(x) for x in numbers[-size:])}")
                total += sum(int(x) for x in numbers[-size:])
            elif operation == '*':
                print(f"Multiplying {numbers[-size:]}: {math.prod(int(x) for x in numbers[-size:])}")
                total += math.prod(int(x) for x in numbers[-size:])
        
        puzzle_matrix.append(puzzle_rows)

    # print(numbers, operations)
    print(total)