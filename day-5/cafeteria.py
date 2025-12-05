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

    print(ranges)
    
    merged_range = [ranges[0]]
    for new_pair in ranges[1:]:
        print(f'merged range: {merged_range}')
        print(f'analyzing new pair: {new_pair}')
        new_callup_start = 0
        new_callup_end = 0
        to_remove = []
        for existing_pair in merged_range:
            print(f'going over existing pair: {existing_pair}')
            # net smaller pair, add it
            if new_pair[0] < existing_pair[0] and new_pair[0] < existing_pair[1] \
                and new_pair[1] < existing_pair[0] and new_pair[1] < existing_pair[1]:
                merged_range.append(new_pair)
                print(f'appending new net smaller pair: {new_pair}')
            # net larger pair, add it
            elif new_pair[0] > existing_pair[0] and new_pair[0] > existing_pair[1] \
                and new_pair[1] > existing_pair[0] and new_pair[1] > existing_pair[1]:
                merged_range.append(new_pair)
                print(f'appending new net larger pair: {new_pair}')
            # extend a pair
            if new_pair[0] > existing_pair[0] and new_pair[0] < existing_pair[1]:
                new_callup_start = existing_pair[0]
                to_remove.append(existing_pair)
            if new_pair[1] > existing_pair[0] and new_pair[1] < existing_pair[1]:
                new_callup_end = existing_pair[1]
                to_remove.append(existing_pair)
            
        if new_callup_start and new_callup_end:
            print(f'Adding new callup: {[new_callup_start, new_callup_end]}')
            merged_range.append([new_callup_start, new_callup_end])

        print(f'removals: {to_remove}')
        for removal in to_remove:
            merged_range.remove(removal)

    print(f'Final ranges: {merged_range}')
