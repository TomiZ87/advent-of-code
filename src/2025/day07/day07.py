def load():
    return open("./src/2025/day07/input.txt", mode="r", encoding="UTF-8").read().split('\n')

def solve(manifold):
    num_collisions = 0
    beam_paths = [1 if x == "S" else 0 for x in manifold[0]]
    for row in manifold:
        for x, paths_possible in enumerate(beam_paths):
            if row[x] == "^":
                if paths_possible != 0: num_collisions += 1
                beam_paths[x - 1] += paths_possible
                beam_paths[x + 1] += paths_possible
                beam_paths[x] = 0

    return f"Part 1 {num_collisions}\nPart 2 {sum(beam_paths)}"

def main():
    print(solve(load()))

if __name__ == "__main__":
    main()
