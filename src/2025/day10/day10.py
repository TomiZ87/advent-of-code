import itertools
import scipy

def load():
    with open("./src/2025/day10/input.txt", mode="r", encoding="UTF-8") as file:
        data = file.read().split("\n")
        lights, buttons, joltages = [], [], []
        for x in range(len(data)):
            lights.append(data[x][data[x].index("[") + 1: data[x].index("]")])
            raw_buttons = data[x][data[x].index("]") + 2 : data[x].index("{") - 1]
            raw_buttons = raw_buttons.replace(")","").replace("(","").split(" ")
            buttons.append([list(map(int, y.split(','))) for y in raw_buttons])
            joltages.append(list(map(int, data[x][data[x].index("{") + 1 : data[x].index("}")].split(","))))
        
        return lights, buttons, joltages

def toggle_light_button(button_combo, btn_states):
    for button in button_combo:
        for x in button:
            btn_states = btn_states[:x] + ("#" if btn_states[x] == "." else ".") + btn_states[x + 1:]

    return btn_states

def get_min_presses_light(desired_states, buttons):
    min_presses = 100000000
    for index in range(len(desired_states)):

        for size in range(1, len(buttons)):
            for button_combination in itertools.combinations(buttons, size):
                if desired_states == toggle_light_button(button_combination, '.' * len(desired_states)) and min_presses > len(button_combination):
                    min_presses = len(button_combination)

        return min_presses

# Note to myself: https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
def get_min_presses_joltage(joltages, buttons):
    A = []
    for _ in range(len(joltages)):
        A.append([0] * len(buttons))
        
    for x, button in enumerate(buttons):
        for light_toggle in button:
            A[light_toggle][x] = 1

    return round(sum(scipy.optimize.linprog([1] * len(buttons), A_eq=A, b_eq=joltages, integrality=1).x))

def main():
    lights, buttons, joltages = load()
    total_min_presses_light = total_min_presses_joltage = 0
    for x in range(len(lights)):
        total_min_presses_light += get_min_presses_light(lights[x], buttons[x])
        total_min_presses_joltage += get_min_presses_joltage(joltages[x], buttons[x])

    print("Part 1", total_min_presses_light)
    print("Part 2", total_min_presses_joltage)

if __name__ == "__main__":
    main()