import re

DATA_PATH = "./day_3/data.txt"
MUL_SEQUENCE = r"mul\(\d+,\d+\)"
CONTROL_SEQUENCE = r"\b(do\(\)|don't\(\))"


def _load_data(data_path):
    with open(data_path, 'r') as file:
        return file.read()


def _find_sequences_with_index(text, pattern):
    matches = [{"seq": match.group(), "index": match.start()} for match in re.finditer(pattern, text)]
    return matches


def _compute_multiplication(mult):
    split_para = mult.split("(")
    split_comma = split_para[1].split(",")
    first = int(split_comma[0])
    second = int(split_comma[1][:-1])
    return first * second


def solve_first_puzzle():
    data = _load_data(DATA_PATH)
    multiplications = _find_sequences_with_index(data, MUL_SEQUENCE)
    total = 0
    for mult in multiplications:
        total += _compute_multiplication(mult["seq"])
    print(total)


def solve_second_puzzle():
    data = _load_data(DATA_PATH)
    enabled = True
    total_sum = 0

    for token in re.finditer(f"{MUL_SEQUENCE}|{CONTROL_SEQUENCE}", data):
        match = token.group()

        if "do()" in match:
            enabled = True
        elif "don't()" in match:
            enabled = False
        else:
            if enabled:
                total_sum += _compute_multiplication(match)

    print(total_sum)


solve_first_puzzle()
solve_second_puzzle()
