from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-4/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def check_adjacent_coords(matrix: list, i: int, j: int, n: int, symbol='@'):
    """Checks adjacent coords which are n distances away from (i, j) for presence of symbol"""

    starting_point = matrix[i][j]
    paper_count = 0

    for a in range(i - n, i + n + 1):
        for b in range(j - n, j + n + 1):
            if a == i and b == j:
                # we are on the source coord
                # print('X', end=" ")
                # print((a,b), end='')
                pass
            elif a < 0 or b < 0 or a >= len(matrix) or b >= len(matrix[0]):
                # we are outside the matrix
                # print('O', end=' ')
                # print((a,b), end='')
                pass
            else:
                # check for symbol
                # print(matrix[a][b], end=" ")
                if matrix[a][b] == '@':
                    paper_count += 1

                # print((a,b), end='')
        # print("\n")

    return paper_count



if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    matrix = [x for x in puzzle_input.split('\n')]

    # The forklifts can only access a roll of paper if there are fewer than four rolls of paper in adjacent positions
    
    print(matrix)

    matrix = [list(x) for x in matrix]

    total_removed = 0
    while(True):
        reachable_count = 0
        removable = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print(matrix[i][j], end=" ")
                if matrix[i][j] == '@':
                    paper_count = check_adjacent_coords(matrix, i, j, 1)
                    if paper_count < 4:
                        reachable_count += 1
                        removable.append((i,j))
            # print("\n")
    
        print(f"Reachable count: {reachable_count}")
        total_removed += reachable_count

        if removable:
            for i, j in removable:
                matrix[i][j] = '.'
        else:
            break

print(f"Total removed: {total_removed}")