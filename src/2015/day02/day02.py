def load():
    with open("./src/2015/day02/input.txt", mode="r", encoding="UTF-8") as file:
        rows = file.readlines()
        for row in range(len(rows)):
            rows[row] = rows[row].strip('\n').split('x')
        return rows

def main():
    sum_sides = 0
    ribbons = 0
    file = load()
    for row in file:
        row = [int(x) for x in row]
        row.sort()
        sides = [row[0]*row[1], row[1]*row[2], row[0]*row[2]]
        sum_sides += (2*sides[0] + 2*sides[1] + 2*sides[2] + min(sides))
        ribbons += (2*row[0] + 2*row[1] + (row[0]*row[1]*row[2]))
    
    print("Part 1", sum_sides)
    print("Part 2", ribbons)
    
if __name__ == "__main__":
    main()