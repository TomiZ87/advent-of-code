def load():
    with open("./src/2025/day11/input.txt", mode="r", encoding="UTF-8") as file:
        devices = dict()
        for row in file.readlines():
            device, paths = row.strip().split(":")
            devices[device] = paths.strip().split()

        return devices

def count_paths(current_device, desired_device):
    total = 0
    if current_device == desired_device:
        return 1
    elif current_device == "out":
        return 0
    elif current_device + desired_device in cache:
        return cache[current_device + desired_device]

    for next_device in devices[current_device]:
        total += count_paths(next_device, desired_device)
        
    cache[current_device + desired_device] = total

    return total

def main():
    global devices, cache
    devices, cache = load(), dict()
    print("Part 1", count_paths("you", "out"))
    # We can get the paths through fft and dac by calculating paths between the segments and using combinatorics 
    print("Part 2", count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))

if __name__ == "__main__":
    main()
