def transform(value):
    if len(value) == 1:
        return "1" + str(value)
    new_value = ""
    prev_char = value[0:1]
    count = 1
    for char in value[1:]:
        if char == prev_char:
            count += 1
        else:
            new_value += str(count) + prev_char
            prev_char = char
            count = 1
    if count > 0:
        new_value += str(count) + prev_char
    return new_value


start = "1113122113"

for x in range(50):
    start = transform(start)

end = start

print(len(end))

