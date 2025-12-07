from pathlib import Path
import math
PUZZLE_INPUT_PATH = Path("day-7/sample-puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)
    matrix = [list[str](x) for x in puzzle_input.split('\n')]
    rows = len(matrix)
    cols = len(matrix[0])
    print(f"Rows: {rows}, Cols: {cols}")

    print(puzzle_input)
    
    # find starting point
    for i in range(cols):
        cell = matrix[0][i]
        if cell == 'S':
            start = i
            matrix[1][start] = '|'
            print(f"Starting point: {start}")
            break  
    
    splits = []
    for i in range(1, rows - 1):
        for j in range(cols):

            if matrix[i][j] == '^':
                if matrix[i - 1][j] == '|':
                    # make a split
                    splits.append((i, j))
                    matrix[i][j - 1] = '|'
                    matrix[i + 1][j - 1] = '|'
                    matrix[i][j + 1] = '|'
                    matrix[i + 1][j + 1] = '|'

            if matrix[i][j] == '|' and matrix[i + 1][j] == '.':
                matrix[i + 1][j] = '|'
    
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end='')
        print()

    print(f'Splits: {splits[:4]}...')
    print(f'Total splits: {len(splits)}')