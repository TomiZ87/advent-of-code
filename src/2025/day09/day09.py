def load():
    with open("./src/2025/day09/input.txt", mode="r", encoding="UTF-8") as file:
        read_lines = file.read().split('\n')
        for row in range(len(read_lines)):
            read_lines[row] = read_lines[row].split(',')
            read_lines[row][0], read_lines[row][1] = int(read_lines[row][0]), int(read_lines[row][1])
        
        return read_lines

def part1(grid):
    areas = []
    for x in range(len(grid)):
        for y in range(x + 1, len(grid)):
            areas.append((abs(grid[x][0] - grid[y][0]) + 1) * (abs(grid[x][1] - grid[y][1]) + 1))
    
    return max(areas)

def part2(grid):
    max_area = 0
    for x in range(len(grid)):
        for y in range(x + 1, len(grid)):
            area = (abs(grid[x][0] - grid[y][0]) + 1) * (abs(grid[x][1] - grid[y][1]) + 1)
            if max_area < area:
                valid = True
                for z in range(len(grid)):
                    if not ((grid[z][1] >= max(grid[x][1], grid[y][1]) and grid[(z + 1) % len(grid)][1] >= max(grid[x][1], grid[y][1])) or
                            (grid[z][0] >= max(grid[x][0], grid[y][0]) and grid[(z + 1) % len(grid)][0] >= max(grid[x][0], grid[y][0])) or
                            (grid[z][1] <= min(grid[x][1], grid[y][1]) and grid[(z + 1) % len(grid)][1] <= min(grid[x][1], grid[y][1])) or
                            (grid[z][0] <= min(grid[x][0], grid[y][0]) and grid[(z + 1) % len(grid)][0] <= min(grid[x][0], grid[y][0]))):
                        valid = False
                        break
                if valid:
                    max_area = area
    
    return max_area

def main():
    print("Part 1", part1(load()))
    print("Part 2", part2(load()))

if __name__ == "__main__":
    main()
