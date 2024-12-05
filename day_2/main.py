import numpy as np

DATA_PATH = "./day_2/data.txt"

def _load_data(data_path):
    lines = []
    with open(data_path, 'r') as file:
        for line in file:
            split_skip = line.split("\n")
            split_space = split_skip[0].split(" ")
            list_of_int = [int(item) for item in split_space]
            lines.append(list_of_int)
    return lines


def _is_strictly_increasing(numbers):
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))


def _is_strictly_decreasing(numbers):
    return all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))


def _are_differences_in_range(numbers, min_diff=1, max_diff=3):
    differences = abs(np.diff(numbers))
    if (min_diff<= differences).all() and (differences <= max_diff).all():
        return True


def _is_report_safe(report):
    if _is_strictly_decreasing(report) or _is_strictly_increasing(report):
        if _are_differences_in_range(report):
            return True


def solve_first_puzzle(data_path):
    data = _load_data(data_path)
    total_safe_reports = 0
    for report in data:
        if _is_report_safe(report):
            total_safe_reports +=1

    print(total_safe_reports)


def solve_second_puzzle(data_path):
    data = _load_data(data_path)
    total_safe_reports = 0
    for report in data:
        total_safe_modified_reports = 0
        if _is_report_safe(report):
            total_safe_modified_reports += 1
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if _is_report_safe(modified_report):
                total_safe_modified_reports += 1
        if total_safe_modified_reports > 0:
            total_safe_reports += 1
    print(total_safe_reports)


solve_first_puzzle(DATA_PATH)
solve_second_puzzle(DATA_PATH)

