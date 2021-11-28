import re

filename = "input.txt"
data = open(filename, "r")

pad = 60
total_length_string = 0
total_length_encoded = 0
for line in data:
    line = line.strip()
    length_string = len(line)
    padding = (pad+1 if length_string<10 else pad) - length_string
    print(line, padding * " ", length_string, end="\t")
    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    line = '"' + line + '"'
    length_encoded = len(line)
    padding = (pad+1 if length_encoded < 10 else pad) - length_encoded
    print(line, padding * " ", length_encoded)
    total_length_string += length_string
    total_length_encoded += length_encoded

print("\ntotal_length_string=", total_length_string, " ; total_length_encoded=", total_length_encoded, " ; ", total_length_encoded, "-", total_length_string, "=", total_length_encoded - total_length_string)


