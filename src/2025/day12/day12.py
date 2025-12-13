def load():
    with open("./src/2025/day12/input.txt") as data:
        standard_areas = []
        *shapes, instructions = data.read().split("\n\n")
        standard_areas = [shapes[x].count("#") for x in range(len(shapes))]
        instructions = instructions.split("\n")

        for x in range(len(instructions)):
            instructions[x] = instructions[x].split()
            instructions[x][0] = int(instructions[x][0].split("x")[0]) * int(instructions[x][0].split("x")[1].strip(":"))

        return standard_areas, instructions

def part1():
    standard_areas, instructions = load()
    total_presents_fit = 0
    for x in range(len(instructions)):
        space_needed = 0
        for index, value in enumerate(instructions[x]):
            if index != 0: space_needed += standard_areas[index - 1] * int(value)
        if instructions[x][0] - space_needed >= 0: total_presents_fit += 1
    # I am suprised this worked, because according to the description I would have expected a more robust try method to fit the presents (I was just playing arund and I just tried this simplified solution and it worked lmao)
    return total_presents_fit

def main():
    print("Part 1", part1(), "\nNo Part 2 :))")

if __name__ == "__main__":
    main()
