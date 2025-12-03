def load():
    with open("./src/2025/day03/input.txt", mode="r", encoding="UTF-8") as file:
        return file.read().splitlines()

# Did something similar in the past (tho iteratively this time)
def calculate_joltages(banks, digits):
    joltages = 0
    for bank in banks:
        picked_digits = []
        start = 0

        for digit in range(digits):
            remaining = digits - digit - 1
            best_digit, best_index = '-1', -1 # the best element could be found & simplified using lambda, but i need to practice

            for x in range(start, len(bank) - remaining):
                if int(bank[x]) > int(best_digit):
                    best_digit = bank[x]
                    best_index = x

            picked_digits.append(best_digit)
            start = best_index + 1 
        joltages += int("".join(picked_digits))
    return joltages

def main():
    print("Part 1", calculate_joltages(load(), 2))
    print("Part 2", calculate_joltages(load(), 12))

if __name__ == "__main__":
    main()
