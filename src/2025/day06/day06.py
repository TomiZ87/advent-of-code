def load(part2 = False):
    with open("./src/2025/day06/input.txt", mode="r", encoding="UTF-8") as file:
        data = file.readlines()
        for row in range(len(data)):
            if part2 == False:
                data[row] = data[row].strip('\n').split()
            else:
                data[row] = data[row][::-1].strip('\n')

        return data

def part1(data):
    total = 0
    for x in range(len(data[0])):
        if data[-1][x] == '*':
            total += int(data[0][x]) * int(data[1][x]) * int(data[2][x]) * int(data[3][x])
        else:
            total += int(data[0][x]) + int(data[1][x]) + int(data[2][x]) + int(data[3][x])

    return total

def multiply_list(input_list):
    result = 1
    for x in input_list:
        result *= int(x)

    return result

def part2(data):
    total, numbers = 0, []
    for x in range(len(data[0])):
        number = data[0][x] + data[1][x] + data[2][x] + data[3][x]
        if number != '    ':
            numbers.append(number)
            if data[-1][x] == '*':
                total += multiply_list(numbers)
            elif data[-1][x] == '+':
                total += sum([int(x) for x in numbers])
        else:
            numbers.clear()

    return total

def main():
    print("Part 1", part1(load()))
    print("Part 2", part2(load(True)))

if __name__ == "__main__":
    main()
