from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-1/puzzle-input.txt")

def get_puzzle_input(path: Path) -> str:
    with open(path, 'r') as f:
        raw_input = f.read()
    return raw_input

def parse_instructions(instructions: str) -> list:
    current_arrow_point = 50
    running_count = 0
    rotation_hits = 0

    for instruction in instructions:
        print(f'Current arrow point: {current_arrow_point}')
        print(f'Current instruction: {instruction}')

        direction = instruction[0]
        
        count = int(instruction[1:])
        turn_count = count / 100
        count_leftover = count % 100

        if direction == 'R':
            arrow_point_sum = current_arrow_point + count_leftover
            if arrow_point_sum > 99:
                new_arrow_point = arrow_point_sum - 100
            else:
                new_arrow_point = arrow_point_sum

            if arrow_point_sum > 100:
                rotation_hits += 1
                print(f"Adding an overclock hit")
        
        elif direction == 'L':
            arrow_point_sum = current_arrow_point - count_leftover
            if arrow_point_sum < 0:
                new_arrow_point = (100 + arrow_point_sum)
            else:
                new_arrow_point = arrow_point_sum

            if arrow_point_sum < 0 and current_arrow_point != 0:
                rotation_hits += 1
                print(f"Adding an overclock hit")

        if int(turn_count):
            rotation_hits += int(turn_count)
            print(f'Adding {int(turn_count)} rotation hits')
        
        current_arrow_point = new_arrow_point
        print(f"New arrow point: {new_arrow_point}")
        if new_arrow_point == 0:
            running_count += 1


    
    return running_count, rotation_hits

    
if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    instructions = puzzle_input.split('\n')

    running_count, rotation_hits = parse_instructions(instructions)
    
    print(f'Count of zeroes: {running_count}')
    print(f'Count of rotations: {rotation_hits}')

    print(f'Totals: {running_count + rotation_hits}')
