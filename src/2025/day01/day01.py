def load():
    with open("./src/2025/day01/input.txt", mode="r", encoding="UTF-8") as file:
        rows = file.readlines()
        for row in range(len(rows)):
            rows[row] = rows[row].strip('\n')
        return rows

def part1(file):
    num = 50
    counter = 0
    for row in file:
        num += (int(row[1:])) if row[0] == 'R' else -int(row[1:])
        if num % 100 == 0: 
            counter += 1
    
    print("Part 1", counter)

def part2(file):
    num = 50
    counter = 0
    for row in file:
        to_change = int(row[1:])
        if row[0] == 'L':
            to_change = -to_change
            counter += ((num + to_change) % 100 == 0) - ((num % 100) == 0)

        num += to_change
        counter += abs((num - to_change) // 100 - num // 100)
    print("Part 2", counter)

def main():
    file = load()
    part1(file)
    part2(file)

if __name__ == "__main__":
    main()