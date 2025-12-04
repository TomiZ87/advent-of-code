def load():
    with open("./src/2025/day04/input.txt", mode="r", encoding="UTF-8") as file:
        return file.read().splitlines()

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def check_accessibility(grid):
    accessible_pos = list()
    for row in range(len(grid)):
        for pos in range(len(grid[row])):
            if grid[row][pos] == "@":
                nonaccessible_cells = 0
                for row_offset, pos_offset in DIRECTIONS:
                    if 0 <= (row + row_offset) < len(grid) and 0 <= (pos + pos_offset) < len(grid[row]):
                        if grid[row + row_offset][pos + pos_offset] == "@":
                            nonaccessible_cells += 1
                
                if nonaccessible_cells < 4:
                    accessible_pos.append((row, pos))

    return accessible_pos

def remove_rolls(grid):
    all_accessible, current = 0, 1
    while (current > 0):
        current = 0
        changed_grid = check_accessibility(list(grid))
        current = len(changed_grid)
        all_accessible += current
        for row, pos in changed_grid:
            grid[row] = grid[row][:pos] + "X" + grid[row][pos+1:]
    return all_accessible

def main():
    print("Part 1", len(check_accessibility(load())))
    print("Part 2", remove_rolls(load()))

if __name__ == "__main__":
    main()
