from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-9/sample-puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def matrixify(puzzle_input):
    coords = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    x_coords, y_coords = zip(*coords)

    cols = max([int(x) for x in x_coords]) + 2
    rows = max([int(y) for y in y_coords]) + 2

    matrix = [['.'] * cols for _ in range(rows)]

    for coord in coords:
        matrix[coord[1]][coord[0]] = '#'

    return matrix, coords

def calc_area(coord_1: tuple, coord_2: tuple) -> int:
    return (abs(coord_1[0] - coord_2[0]) + 1) * (abs(coord_1[1] - coord_2[1]) + 1)

if __name__ == '__main__':
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    matrix, coords = matrixify(puzzle_input)

    # for row in range(len(matrix)):
    #     for col in range(len(matrix[0])):
    #         print(matrix[row][col], end='')
    #     print()

    max_area = 0
    max_coords = []
    for coord in coords:
        for second_coord in coords:
            rect_area = calc_area(coord, second_coord)
            if max_area < rect_area:
                max_area = rect_area
                max_coords = [coord, second_coord]

    print(f'Found largest rectangle of area {max_area} between points {max_coords[0]} and {max_coords[1]}')