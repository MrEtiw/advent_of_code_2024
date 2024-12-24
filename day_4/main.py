DATA_PATH = "./day_4/data.txt"
DIRECTIONS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1)
]
WORD_TO_FIND = "XMAS"

"""
def _load_data(data_path):
    lines = []
    with open(data_path, 'r') as file:
        for line in file:
            lines.append(line.split("\n")[0])
    return lines


def _is_direction_compatible(position, direction, grid_size):
    x = position[0]
    y = position [1]
    x_dir = direction[0]
    y_dir = direction[1]
    nb_rows = grid_size[0]
    nb_cols = grid_size[1]

    len_word = len(WORD_TO_FIND)

    if (x + (len_word-1)*x_dir < 0) or (x + (len_word-1)*x_dir > nb_cols):
        return False
    if (y + (len_word-1)*y_dir < 0) or (y + (len_word-1)*y_dir > nb_rows):
        return False
    return True




def solve_first_puzzle():
    data = _load_data(DATA_PATH)
    nb_rows = len(data)
    nb_cols = len(data[0])
    size = (nb_rows, nb_cols)
    for row in range(nb_rows):
        for col in range(nb_cols):
            position = (row, col)
            elem = data[row][col]
            if elem == WORD_TO_FIND[0]:
                # look for each direction
                for direction in DIRECTIONS:
                    if _is_direction_compatible(position, direction, size):
                        word =

            elif elem == WORD_TO_FIND[-1]:
                # look for each reverse direction
            else:
                # not the end nor start of the word to find



solve_first_puzzle()
"""





# Taken from https://github.com/fuglede/adventofcode/blob/master/2024/day04/solutions.py
# My solution was getting way too convoluted
# Learnings: create a dict, where the keys are the indexes, and store the string for each direction!
# Brillant, greatly reduces search time


from collections import defaultdict
from itertools import product

with open(DATA_PATH) as f:
    ls = f.read().strip().split("\n")


boardz = defaultdict(str)
boardz |= {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
octdir = {i + 1j * j for (i, j) in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}}

# Part 1
print(
    sum(
        [boardz[z + i * dz] for i in range(4)] == ["X", "M", "A", "S"]
        for z in list(boardz.keys())
        for dz in octdir
    )
)


# Part 2
res = 0
for z in list(boardz.keys()):
    if boardz[z] == "A":
        corners = [
            boardz[z + 1 + 1j],
            boardz[z + 1 - 1j],
            boardz[z - 1 - 1j],
            boardz[z - 1 + 1j],
        ]
        if (
            corners.count("M") == 2
            and corners.count("S") == 2
            and boardz[z - 1 - 1j] != boardz[z + 1 + 1j]
        ):
            res += 1
print(res)