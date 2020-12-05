# Solution to Day 4

import re

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def read_input():
    return open("input-4.txt", "r").read()


def isvalid_1(fields):
    missing = []
    for k in keys:
        if k not in fields:
            missing += [k]
    return len(missing) == 0 or \
            (len(missing) == 1 and missing[0] == "cid")

def isvalid_2(fields):
    return isvalid_1(fields) and \
            isvalid_byr(fields["byr"]) and \
            isvalid_iyr(fields["iyr"]) and \
            isvalid_eyr(fields["eyr"]) and \
            isvalid_hgt(fields["hgt"]) and \
            isvalid_hcl(fields["hcl"]) and \
            isvalid_ecl(fields["ecl"]) and \
            isvalid_pid(fields["pid"])

def isint(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def isvalid_byr(byr):
    return isint(byr) and int(byr)>=1920 and int(byr)<=2002

def isvalid_iyr(iyr):
    return isint(iyr) and int(iyr)>=2010 and int(iyr)<=2020

def isvalid_eyr(eyr):
    return isint(eyr) and int(eyr)>=2020 and int(eyr)<=2030

def isvalid_hgt(hgt):
    h = hgt[:-2]
    unit = hgt[-2:]
    return (unit == "cm" and isint(h) and int(h)>=150 and int(h)<=193) or \
            (unit == "in" and isint(h) and int(h)>=59 and int(h)<=76)

def isvalid_hcl(hcl):
    return hcl[0] == "#" and \
            all([c in "abcdef0123456789" for c in hcl[1:]])

def isvalid_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def isvalid_pid(pid):
    return isint(pid) and len(pid) == 9

def process(text):
    entries = text.split("\n\n")
    pports = []
    for e in entries:
        fields = e.split()
        pports.append({a:b for (a,b) in [f.split(':') for f in fields]})

    n_valid = 0
    for dct in pports:
        if isvalid_1(dct):
            n_valid += 1
    print("one:", n_valid)

    n_valid = 0
    for dct in pports:
        if isvalid_2(dct):
            n_valid += 1
    print("two:", n_valid)


if __name__ == "__main__":
    n_valid = process(read_input())

