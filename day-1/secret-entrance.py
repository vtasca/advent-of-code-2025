from pathlib import Path

PUZZLE_INPUT_PATH = Path("day-1/puzzle-input.txt")

def get_puzzle_input(path: Path) -> str:
    with open(path, 'r') as f:
        raw_input = f.read()
    return raw_input

def parse_instructions(instructions: str) -> list:
    current_arrow_point = 50
    running_count = 0

    for instruction in instructions:
        direction = instruction[0]
        
        count = int(instruction[1:])
        turn_count = count / 100
        count_leftover = count % 100
        
        if direction == 'R':
            if turn_count > 1:
                current_arrow_point = current_arrow_point + count_leftover
            elif current_arrow_point + count > 99:
                current_arrow_point = current_arrow_point + count - 100
            else:
                current_arrow_point += count
            

        elif direction == 'L':
            if turn_count > 1:
                current_arrow_point = current_arrow_point - count_leftover
            elif current_arrow_point - count < 0:
                current_arrow_point = current_arrow_point - count + 100
            else:
                current_arrow_point -= count

        if current_arrow_point > 99:
                    current_arrow_point = current_arrow_point - 100
        elif current_arrow_point < 0:
                    current_arrow_point = 100 - abs(current_arrow_point)

        if current_arrow_point == 0:
            running_count += 1
    
    return running_count

    
if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)

    instructions = puzzle_input.split('\n')

    running_count = parse_instructions(instructions)
    
    print(f'Count of zeroes: {running_count}')

