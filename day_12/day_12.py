import json

data = json.load(open("input.txt", "r"))

numbers = []


def add_numbers(item):
    if isinstance(item, int):
        numbers.append(item)
    elif isinstance(item, dict):
        if 'red' not in item.keys() and 'red' not in item.values():
            for obj in item:
                children = item.get(obj, None)
                if children:
                    add_numbers(children)
    elif isinstance(item, list):
        for obj in item:
            add_numbers(obj)


print(sum(numbers))
