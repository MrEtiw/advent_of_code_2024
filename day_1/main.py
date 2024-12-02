DATA_PATH= "./day_1/data.txt"


def _load_data(data_path):
    lines_1 = []
    lines_2 =[]
    with open(data_path, 'r') as file:
        for line in file:
            split_skip = line.split("\n")
            split_space = split_skip[0].split(" ")
            lines_1.append(int(split_space[0]))
            lines_2.append(int(split_space[-1]))
    return lines_1, lines_2


def solve_first_puzzle(data_path):
    first_list, second_list = _load_data(data_path)
    first_list.sort()
    second_list.sort()
    total_diff = 0
    for first, second in zip(first_list, second_list):
        diff = abs(first-second)
        total_diff += diff
    print(total_diff)


def solve_second_puzzle(data_path):
    first_list, second_list = _load_data(data_path)
    total_product = 0
    for first in first_list:
        frequency = second_list.count(first)
        total_product += first*frequency
    print(total_product)


solve_first_puzzle(DATA_PATH)
solve_second_puzzle(DATA_PATH)
