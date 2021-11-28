import re

filename = "input.txt"
data = open(filename, "r")

total_string_code = 0
total_char_in_memory = 0
for line in data:
    line = line.strip()
    print(line, end=" : ")
    ASCII = re.findall(r'\\x[0-9a-f][0-9a-f]', line)
    quotes = re.findall(r'\\"', line)
    backslash = re.findall(r'\\\\', line)

    count_backslash = len(backslash)
    count_double_quote = len(quotes)
    count_ASCII = len(ASCII)
    string_code = len(line)
    print("ASCII=", count_ASCII, end="; ")
    print("quotes=", count_double_quote, end="; ")
    print("backslashes=", count_backslash, end="; ")
    char_in_memory = string_code - 2 - count_backslash - count_double_quote - (count_ASCII * 3)
    total_char_in_memory += char_in_memory
    total_string_code += string_code
    print("string_code =", string_code, "; char_in_memory", char_in_memory)

print("\ntotal_string_code =", total_string_code, "; total_char_in_memory", total_char_in_memory)
print(total_string_code - total_char_in_memory)