DATA_PATH = "./day_4/data.txt"

def _load_data(data_path):
    lines = []
    with open(data_path, 'r') as file:
        for line in file:
            lines.append(line.split("\n")[0])
    return lines




def solve_first_puzzle():
    data = _load_data(DATA_PATH)
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1)
    ]