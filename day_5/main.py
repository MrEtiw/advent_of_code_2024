DATA_PATH = "./day_5/data.txt"


def _load_data(data_path):
    with open(data_path, 'r') as file:
        content = file.read()
    rules = []
    updates = []
    content_split = content.split('\n')
    for line in content_split:
        if '|' in line:
            first, second = line.split('|')
            rules.append([int(first), int(second)])
        else:
            if line:
                elems = line.split(',')
                updates.append([int(x) for x in elems])
    return rules, updates




def _format_rules(rules):
    formatted_rules = {}
    for rule in rules:
        first = rule[0]
        if first not in formatted_rules.keys():
            formatted_rules[first] = [rule[1]]
        else:
            formatted_rules[first].append(rule[1])
    return formatted_rules


def _is_update_valid(rules, update):
    for i, elem in enumerate(update):
        print(i)
        print(elem)
        conditions = rules.get(elem)
        for condi in conditions:
            condi_index = update.index(condi)
            if condi_index < i:
                return False
    return True


rules, updates = _load_data(DATA_PATH)
rules = _format_rules(rules)

a = _is_update_valid(rules, updates[0])