from pathlib import Path
import math
PUZZLE_INPUT_PATH = Path("day-8/puzzle-input.txt")


def get_puzzle_input(path: Path) -> str:
    with open(path, "r") as f:
        raw_input = f.read()
    return raw_input

def calculate_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2 + (coords1[2] - coords2[2])**2)

def create_distances_matrix(coords_list):
    distances = {coords: {} for coords in coords_list}
    for i, coords in enumerate(coords_list):
        for next_coords in coords_list[i+1:]:
            distance = calculate_distance(coords, next_coords)
            distances[coords][next_coords] = distance
    return distances

def build_connections(smallest, connections, max_connections=10000000000, coords_list=None):
    connection_count = 0
    for distance, coords in smallest.items():
        found_first_coord = False
        found_second_coord = False
        first_coord_index = None
        second_coord_index = None
        if connection_count >= max_connections:
            break
        for index, conn in enumerate(connections):
            if coords[0] in conn:
                found_first_coord = True
                first_coord_index = index
            if coords[1] in conn:
                found_second_coord = True
                second_coord_index = index
        
        if found_first_coord and found_second_coord:
            if first_coord_index != second_coord_index:
                print(f"\n Trying to stick together {connections[first_coord_index]} and {connections[second_coord_index]}")
                connections[first_coord_index] = connections[first_coord_index] + connections[second_coord_index]
                connections.pop(second_coord_index)
            connection_count += 1
        elif found_first_coord and not found_second_coord:
            connections[first_coord_index].append(coords[1])
            print(f"\n Added {coords[1]} to {connections[first_coord_index]} from {coords}")
            connection_count += 1
        elif not found_first_coord and found_second_coord:
            connections[second_coord_index].append(coords[0])
            print(f"\n Added {coords[0]} to {connections[second_coord_index]} from {coords}")
            connection_count += 1
        elif not found_first_coord and not found_second_coord:
            connections.append([coords[0], coords[1]])
            print(f"\n Added {coords[0]} and {coords[1]} to {connections} from {coords}")
            connection_count += 1

        if max([len(x) for x in connections]) == len(coords_list):
                    print(f'found it! after {connection_count} connections')
                    # print(f'last coords: {coords}')
                    return connections, connection_count, [coords[0], coords[1]]

    sorted_connections = sorted([len(x) for x in connections], reverse=True)

    print(f"\n Lengths: {sorted_connections}")

    return math.prod(sorted_connections[:3]), connection_count, [coords[0], coords[1]]

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(PUZZLE_INPUT_PATH)
    
    coords_list = []
    for line in puzzle_input.split('\n'):
        coords = [int(x) for x in line.split(',')]
        coords_list.append(tuple(coords))
    
    # print(f"Coords list: {coords_list}")

    distances = create_distances_matrix(coords_list)

    # create dict of distance: (coord, other_coord) then go down it making connections until we reach the end

    smallest = {}
    for coord, distances in distances.items():
        if distances:
            # print(f"Coord: {coord}")
            ordered_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
            # print(f"Ordered distances: {ordered_distances}")
            for k, v in ordered_distances.items():
                smallest[v] = (coord, k)
    
    smallest = dict(sorted(smallest.items(), key=lambda item: item[0]))

    smallest_subset = list(smallest.keys())[:20]
    smallest_subset_coords = [smallest[x] for x in smallest_subset]

    print(f"\n Smallest subset: {smallest_subset_coords}")

    smallest_distance = list(smallest.keys())[0]

    connections = [list(smallest[smallest_distance])]

    print(f"\n Connections: {connections}")

    result, connection_count, last_coords = build_connections(smallest, connections, max_connections=1000000000, coords_list=coords_list)
    print(f"\n Final result: {result}")
    print(f"\n Connection count: {connection_count}")
    print(f"\n Last coords: {last_coords}")
    print(f"\n Last coords product: {math.prod([x[0] for x in last_coords])}")
