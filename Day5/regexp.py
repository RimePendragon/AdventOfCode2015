import re
import string

alphabet = list(string.ascii_lowercase)

example1 = "ugknbfddgicrmopn"
example2 = "aaa"
example3 = "jchzalrnumimnmhp"
example4 = "haegwjzuvuyypxyu"
example5 = "dvszwmarrgswjxmb"
example6 = "qjhvhtzxzqqjkmpb"
example7 = "xxyxx"
example8 = "uurcxstgmygtbstg"
example9 = "ieodomkazucvgmuy"
example10 = "abhvhtzxzaabkmpb"


x = re.findall("q{1}j{1}", example6)

double_pair = False
for char1 in alphabet:
    for char2 in alphabet:
        x = re.findall(char1+"{1}"+char2+"{1}", example6)
        if len(x) >= 2:
            print(x)


