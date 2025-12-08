from pathlib import Path
PUZZLE_INPUT_PATH = Path("day-7/sample-puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def find_start(matrix):
    # find starting point
    for i in range(len(matrix[0])):
        cell = matrix[0][i]
        if cell == 'S':
            start = i
    return start

def count_splits(matrix, start):
    rows = len(matrix)
    cols = len(matrix[0])

    matrix[1][start] = '|'
    
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
    return splits

def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end='')
        print()

def count_paths(matrix, row, col, memo):
        pos = (row, col)
        
        if pos in memo:
            return memo[pos]
        
        # reached the bottom
        if row + 1 >= len(matrix):
            memo[pos] = 1
            return 1
        
        count = 0
        next_row = row + 1
        
        if next_row < len(matrix):
            cell_below = matrix[next_row][col]
            
            if cell_below == '^':
                left_col = col - 1
                right_col = col + 1
                
                if left_col >= 0 and left_col < len(matrix[next_row]):
                    count += count_paths(matrix, next_row, left_col, memo)
                if right_col >= 0 and right_col < len(matrix[next_row]):
                    count += count_paths(matrix, next_row, right_col, memo)
            elif cell_below == '.' or cell_below == '|':
                count += count_paths(matrix, next_row, col, memo)
        
        memo[pos] = count
        return count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)
    matrix = [list[str](x) for x in puzzle_input.split('\n')]

    start = find_start(matrix)

    splits = count_splits(matrix, start)
    print(f'Number of splits: {len(splits)}')
    
    memo = {}
    total_paths = count_paths(matrix, 1, start, memo)
    print(f'Total paths: {total_paths}')