import string
import re

abc = list(string.ascii_lowercase)
mandatory = []
forbidden = ["i", "o", "l"]
double_chars = []

for x in range(len(abc)):
    for y in range(len(abc)):
        for z in range(len(abc)):
            if x < y < z and z - x < 3:
                mandatory.append(abc[x] + abc[y] + abc[z])

for x in range(len(abc)):
    double_chars.append(abc[x] + abc[x])


def increment_character(password, position):
    character = password[position:position + 1]
    char_index = abc.index(character) + 1
    if char_index >= len(abc):
        char_index = 0
    return password[:position] + abc[char_index] + password[position + 1:]


def increment_password(password):
    length = len(password)
    for position in range(length - 1, -1, -1):
        password = increment_character(password, position)
        character = password[position:position + 1]
        if abc.index(character) > 0:
            return password


def check_password(password):
    good = False
    for check in double_chars:
        x = re.findall(check, password)
        if len(x) > 1:
            good = True
    if good is False:
        return False
    for check in forbidden:
        x = re.findall(check, password)
        if len(x) > 0:
            return False
    good = False
    for chars in mandatory:
        x = re.findall(chars, password)
        if len(x) > 0:
            good = True
    return good


def get_new_password(password):
    while True:
        new_password = increment_password(password)
        if check_password(new_password) is True:
            return new_password
        else:
            password = new_password


print(get_new_password("abcdefgh"))
