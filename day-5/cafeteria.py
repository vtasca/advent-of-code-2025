from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-5/sample-puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def part_1_solution(ranges, ids):
    freshness = {k: 0 for k in ids}

    fresh_count = 0
    for key, value in freshness.items():
        for pair in ranges:
            if value == 0:
                if pair[1] >= key >= pair[0]:
                    freshness[key] = 1

    fresh_count = sum(freshness.values())
    return fresh_count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    range_string, id_string = puzzle_input.split('\n\n')

    ranges = [list(map(int, x.split('-'))) for x in range_string.split('\n')]
    ids = [int(x) for x in id_string.split('\n')]

    # fresh_count = part_1_solution(ranges, ids)
    
    # print(f'Fresh count: {fresh_count}')

    ranges = sorted(ranges)

    print(f"Starting point: {ranges}")

    merged_range = [ranges[0]]
    for index, pair in enumerate(ranges[1:]):
        # is the new pair net larger
        if pair[0] > merged_range[-1][1] and pair[1] > merged_range[-1][1]:
            merged_range.append(pair)

        # is only the right part larger
        if pair[0] < merged_range[-1][1] and pair[1] > merged_range[-1][1]:
            merged_range[-1][1] = pair[1]

        print(f"Step {index}: {merged_range}")

    print(f'Final merged range: {merged_range}')

    target = 0
    for range in merged_range:
        target += range[1] - range[0] + 1

    print(f"Total: {target}")
