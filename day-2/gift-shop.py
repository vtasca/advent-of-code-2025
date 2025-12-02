from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-2/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    intervals = puzzle_input.split(',')

    invalid_ids = []

    for interval in intervals:

        lower_bound = int(interval.split('-')[0])
        upper_bound = int(interval.split('-')[-1])

        for i in range(lower_bound, upper_bound + 1):

            stringified = str(i)
            
            if len(stringified) % 2 == 0:

                for even_number in range(2, len(stringified) + 2, 2):

                    halfway = int(even_number / 2)
                    
                    if stringified[:halfway] == stringified[halfway:]:
                        invalid_ids.append(stringified)
                
    print(f"Invalid IDs: {invalid_ids}")
    print(f"Sum of invalid IDs: {sum([int(x) for x in invalid_ids])}")

