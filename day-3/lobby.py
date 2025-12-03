from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-3/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def calculate_two_digit_joltage(sequences: list) -> list:
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

    return joltages


def find_highest_number(sequence: str, n=0, collection=None, target=2, og_sequence=None) -> int:

    if collection is None:
        collection = {}
        og_sequence = sequence
    
    highest_number = 0
    if n == target:
        print(f"Collection: {collection}")
        ordered_numbers = sorted(collection.values(), key=lambda x: x['index'])
        joltage = int(''.join([str(x['number']) for x in ordered_numbers]))
        return joltage
    else:
        for index, number in enumerate(sequence):
            if int(number) > highest_number:
                highest_number = int(number)
                highest_number_index = index + 1
                og_number_index = og_sequence.index(number) + 1
        n += 1
        collection[n] = {
            "number": highest_number,
            "index": og_number_index
        }

        print(f"Found highest number: {highest_number}")
        if len(sequence[highest_number_index:]) > 0:
            print(f"Fowardly checking the rest of the sequence: {sequence[highest_number_index:]}")
            return find_highest_number(sequence[highest_number_index:], n, collection, target, og_sequence)
        else:
            print(f"Backwardly checking the rest of the sequence: {sequence[:highest_number_index-1]}")
            return find_highest_number(sequence[:highest_number_index-1], n, collection, target, og_sequence)


def sliding_window(sequence: str, window_size: int) -> list:
    return [sequence[i:i+window_size] for i in range(len(sequence) - window_size + 1)]

def foo(sequence: str, target: int):

    print(f"Sequence: {sequence}")
    picks_left = target - 1
    pick_list = []
    pick_index = 0
    for i in range(target):
        window = sequence[pick_index:(len(sequence)-picks_left)]
        print(f"Window: {window}")
        print(f"Making pick number: {picks_left + 1}")
        pick = max(window)
        if len(pick_list) == 0:
            pick_index = sequence.index(pick) + 1
        else:
            pick_index = pick_index + window.index(pick) + 1
        pick_list.append(pick)
        picks_left -= 1
    return pick_list

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    sequences = puzzle_input.split('\n')
    
    print('-' * 100)

    all_joltages = []
    for sequence in sequences:
        joltage_components = foo(sequence, 12)
        joltage = int(''.join([str(x) for x in joltage_components]))
        print(f"Joltage: {joltage}")
        print('-' * 100)
        all_joltages.append(joltage)
    print(f"Sum of all joltages: {sum(all_joltages)}")