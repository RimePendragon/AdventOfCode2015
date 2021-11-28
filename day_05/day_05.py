import string
import re

filename = "input.txt"
data = open(filename, "r")

alphabet = list(string.ascii_lowercase)
vowels = ["a", "e", "i", "o", "u"]
forbidden = ["ab", "cd", "pq", "xy"]


def is_nice(check):
    for char in forbidden:
        if check.count(char):
            return False

    double_char = False
    for char in alphabet:
        if check.count(char + char) > 0:
            double_char = True

    three_vowels = False
    vowel_count = 0
    for char in vowels:
        if check.count(char) > 0:
            vowel_count += check.count(char)
    if vowel_count >= 3:
        three_vowels = True

    if double_char is True and three_vowels is True:
        return True
    else:
        return False


def is_nicer(check):
    double_pair = False
    spaced_pair = False
    for char1 in alphabet:
        for char2 in alphabet:
            x = re.findall(char1 + "{1}" + char2 + "{1}", check)
            if len(x) >= 2:
                double_pair = True
            if check.count(char1 + char2 + char1) > 0:
                spaced_pair = True

    if double_pair is True and spaced_pair is True:
        return True
    else:
        return False



example1 = "ugknbfddgicrmopn"
example2 = "aaa"
example3 = "jchzalrnumimnmhp"
example4 = "haegwjzuvuyypxyu"
example5 = "dvszwmarrgswjxmb"

print("========= is_nice =========")
print(example1, "=", is_nice(example1))
print(example2, "=", is_nice(example2))
print(example3, "=", is_nice(example3))
print(example4, "=", is_nice(example4))
print(example5, "=", is_nice(example5))

example6 = "qjhvhtzxzqqjkmpb"
example7 = "xxyxx"
example8 = "uurcxstgmygtbstg"
example9 = "ieodomkazucvgmuy"
example10 = "abhvhtzxzaabkmpb"

print("========= is_nicer =========")
print(example6, "=", is_nicer(example6))
print(example7, "=", is_nicer(example7))
print(example8, "=", is_nicer(example8))
print(example9, "=", is_nicer(example9))
# print(example10, "=", is_nicer(example10))

nice_counter = 0
nicer_counter = 0
counter = 0

for line in data:
    counter += 1
    print("\rCalculating(", counter, ")", end="")
    if is_nice(line):
        nice_counter += 1
    if is_nicer(line):
        nicer_counter += 1

print("\nNice string total=", nice_counter)
print("Nicer string total=", nicer_counter)
