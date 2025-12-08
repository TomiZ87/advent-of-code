import math
def load():
    with open("./src/2025/day08/input.txt", mode="r", encoding="UTF-8") as file:
        read_lines = file.read().split('\n')
        for row in range(len(read_lines)):
            read_lines[row] = read_lines[row].split(',')
            read_lines[row][0], read_lines[row][1], read_lines[row][2] = int(read_lines[row][0]), int(read_lines[row][1]), int(read_lines[row][2])
        
        return read_lines

def solve(boxes, part2 = False):
    pairs, circuits = [], []
    for x in range(len(boxes)):
        circuits.append({tuple(boxes[x])})
        for y in range(x + 1, len(boxes)):
            pairs.append((math.dist(tuple(boxes[x]), tuple(boxes[y])), tuple(boxes[x]), tuple(boxes[y])))
    pairs.sort()

    for index, (_, jbox1, jbox2) in enumerate(pairs):
        if index == 1000 and not part2: 
            lens = sorted([len(x) for x in circuits])
            return lens[-1] * lens[-2] * lens[-3]

        found_circuit1, found_circuit2 = -1, -1
        for i, circuit in enumerate(circuits):
            if jbox1 in circuit: 
                found_circuit1 = i
            if jbox2 in circuit: 
                found_circuit2 = i

        if circuits[found_circuit1] != circuits[found_circuit2]:
            circuits[found_circuit1] |= circuits[found_circuit2]
            circuits.remove(circuits[found_circuit2])

        if len(circuits) == 1:
            return jbox1[0] * jbox2[0]

def main():
    print("Part 1", solve(load()))
    print("Part 2", solve(load(), True))

if __name__ == "__main__":
    main()
