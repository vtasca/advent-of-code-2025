from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-3/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    sequences = puzzle_input.split('\n')

    joltages = []

    for sequence in sequences:

        # find the highest number that's not on the last position
        highest_number = 0
        for index, number in enumerate(sequence):
            if index != len(sequence) - 1:
                if int(number) > highest_number:
                    highest_number = int(number)
                    highest_number_index = index + 1
                    
        # then find the highest number after that
        second_highest_number = 0
        for index, number in enumerate(sequence[highest_number_index:]):
            if int(number) > second_highest_number:
                second_highest_number = int(number)
        
        joltage = int(f"{highest_number}{second_highest_number}")
        joltages.append(joltage)

    print(f"Joltages: {joltages}")
    print(f"Sum of joltages: {sum(joltages)}")
