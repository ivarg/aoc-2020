# Solution to Day 5

from functools import reduce
import operator

def read_input():
    return open("input-6.txt", "r").read()

def process_1(inpt):
    groups = inpt.split("\n\n")
    total = 0
    for group in groups:
        ans = {c:1 for g in group.split() for c in g}
        total += reduce(operator.add, ans.values())
    print("one:", total)

def process_2(inpt):
    groups = inpt.split("\n\n")
    total = 0
    for group in groups:
        ans = list(reduce(lambda x,y: operator.and_(set(x),set(y)), group.split()))
        total += len(ans)
    print("two:", total)

if __name__ == "__main__":
    process_1(read_input())
    process_2(read_input())


