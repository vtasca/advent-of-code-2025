from pathlib import Path
from collections import defaultdict

PUZZLE_INPUT_PATH = Path("day-9/sample-puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def coords_to_dict(puzzle_input):
    points = defaultdict(list)

    for line in puzzle_input.splitlines():
        x, y = map(int, line.split(','))
        points[x].append(y)

    return dict(points)

def matrixify(puzzle_input):
    coords = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]
    x_coords, y_coords = zip(*coords)

    cols = max([int(x) for x in x_coords]) + 2
    rows = max([int(y) for y in y_coords]) + 2

    matrix = [['.'] * cols for _ in range(rows)]

    for coord in coords:
        matrix[coord[1]][coord[0]] = '#'

    return matrix

def calc_area(coord_1: tuple, coord_2: tuple) -> int:
    return (abs(coord_1[0] - coord_2[0]) + 1) * (abs(coord_1[1] - coord_2[1]) + 1)

if __name__ == '__main__':
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    coords = [tuple(map(int, line.split(','))) for line in puzzle_input.splitlines()]

    coord_dict = coords_to_dict(puzzle_input)

    coords_x = [int(line.split(',')[0]) for line in puzzle_input.splitlines()]
    coords_y = [int(line.split(',')[1]) for line in puzzle_input.splitlines()]

    print(sorted(coords))
    print(coord_dict)

    min_x = min(coords_x)
    max_x = max(coords_x)

    max_distance = 0
    for min_y in coord_dict[min_x]:
        for max_y in coord_dict[max_x]:
            distance = abs(min_y - max_y)
            if distance > max_distance:
                max_distance = distance
                corners = [[min_x, min_y], [max_x, max_y]]

    area = calc_area(corners[0], corners[1])
        

    print(f'Found largest rectangle of area {area} between points {corners[0]} and {corners[1]}')