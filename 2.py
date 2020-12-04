# Solution for Day 2

import re

def read_input():
    inpt = []
    with open("input-2.txt", "r") as f:
        return f.readlines()

def isvalid_1(min, max, c, pw):
    return min <= pw.count(c) <= max

def isvalid_2(p1, p2, c, pw):
    v1 = pw[p1-1] == c
    v2 = pw[p2-1] == c
    return v1 != v2

def process(lines):
    valid_1, valid_2 = 0, 0
    for l in lines:
        m = re.match(r"(\d+)-(\d+)\s(\w):\s(\w+)", l)
        min, max, c, pw = m[1], m[2], m[3], m[4]
        if isvalid_1(int(min), int(max), c, pw):
            valid_1 = valid_1+1
        if isvalid_2(int(min), int(max), c, pw):
            valid_2 = valid_2+1

    return valid_1, valid_2


if __name__ == "__main__":
    lines = read_input()
    print(process(lines))
