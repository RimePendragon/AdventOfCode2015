import re
import os
import sys

filename = "example.txt"
data = open(os.path.join(sys.path[0], filename ), "r")

total_length_string = 0
total_length_in_memory = 0
for line in data:
    line = line.strip()
    print(line, end="")
    line = line[1:-1]
    ASCII = re.findall(r'\\x[0-9a-f]{2}', line)
    quotes = re.findall(r'\\"', line)
    backslash = re.findall(r'\\\\', line)
    count_backslash = len(backslash)
    count_double_quote = len(quotes)
    count_ASCII = len(ASCII)
    length_string = len(line) + 2
    length_in_memory = length_string - 2 - count_backslash - count_double_quote - (count_ASCII * 3)
    total_length_in_memory += length_in_memory
    total_length_string += length_string
    # if count_backslash > 0: print("count_backslash=", count_backslash, end="; ")
    # if count_double_quote > 0: print("count_double_quote=", count_double_quote, end="; ")
    # if count_ASCII > 0: print("count_ASCII=", count_ASCII*3, end="; ")
    padding = 20 - length_string
    print(padding * " ", "length_string =", length_string, "length_in_memory", length_in_memory)

print("\ntotal_length_string =", total_length_string, "; total_length_in_memory =", total_length_in_memory, "; ", total_length_string, "-", total_length_in_memory, "=", total_length_string - total_length_in_memory)
