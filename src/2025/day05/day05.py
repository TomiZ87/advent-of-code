def load():
    with open("./src/2025/day05/input.txt", mode="r", encoding="UTF-8") as file:
        data = file.read().split("\n\n")
        ranges = data[0]
        ranges = ranges.split("\n")
        for x in range(len(ranges)):
            ranges[x] = ranges[x].split("-")
            ranges[x][0] = int(ranges[x][0])
            ranges[x][1] = int(ranges[x][1])

        ingredients = data[1]
        ingredients = ingredients.split("\n")
        for x in range(len(ingredients)):
            ingredients[x] = int(ingredients[x])
        return ranges, ingredients

def check_in_range(ranges, ingredients):
    fresh_ingredients = 0
    for ingredient in ingredients:
        for x in ranges:
            if x[0] <= ingredient <= x[1]:
                fresh_ingredients += 1
                break
    return fresh_ingredients

def merge_intervals(ranges):
    merged_intervals = []
    ranges.sort()
    merged_intervals.append(ranges[0])
    for x in range(1, len(ranges)):
        current = ranges[x]
        
        if current[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max([current[1], merged_intervals[-1][1]])
        else:
            merged_intervals.append(current)
    return merged_intervals

def check_all_valid_ids(ranges):
    valid_ids = 0
    for x in ranges:
        valid_ids += (x[1] - x[0]) + 1
    return valid_ids

def main():
    ranges, ingredients = load()
    print("Part 1", check_in_range(ranges, ingredients))
    print("Part 2", check_all_valid_ids(merge_intervals(ranges)))

if __name__ == "__main__":
    main()
