import re

def load():
    with open("./src/2025/day02/input.txt", mode="r", encoding="UTF-8") as file:
        ids = file.read().strip('\n').split(',')
        for id in range(len(ids)):
            ids[id] = ids[id].split('-')
        return ids

def part1(file):
    invalid_sum = 0
    for x in file:
        for y in range(int(x[0]), int(x[1]) + 1):
            y = str(y)
            if len(str(y)) % 2 == 0:
                if y[:int(len(y) / 2)] == y[int(len(y) / 2):]:  
                    invalid_sum += int(y)
    # Also could be done by just matching r"^(.+)\1$", but I did not want to redo this again :))
    print("Part 1", invalid_sum)

def part2(file):
    invalid_sum = 0
    for x in file:
        for y in range(int(x[0]), int(x[1]) + 1):
            pattern = re.compile(r"^(.+)\1+$")
            if pattern.match(str(y)) != None:
                invalid_sum += y
    print("Part 2", invalid_sum)

def main():
    file = load()
    part1(file)
    part2(file)

if __name__ == "__main__":
    main()