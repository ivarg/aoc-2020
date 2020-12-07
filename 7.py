# Solution to Day 7

# from functools import reduce
# import operator
import re

def read_input():
    return open("input-7.txt", "r").readlines()

def process_1(rules):
    bags = {}
    rlist = [r.strip().split("contain") for r in rules]
    for r in rlist:
        bag = r[0][:-5].strip()
        contains = re.findall("\d (\w+ \w+)", r[1])
        # print(bag, contains)
        for b in contains:
            if b not in bags:
                bags[b] = []
            bags[b].append(bag)

    # print(bags)
    nodes = {b:None for b in bags["shiny gold"]}
    Q = bags["shiny gold"]
    while len(Q)>0:
        color = Q[0]
        Q = Q[1:]
        if color in bags:
            Q.extend(bags[color])
        nodes[color]=None

    print("one:", len(nodes))

def rec(bags, color):
    if color not in bags:
        return 1
    res = [rec(bags, c)*int(cnt) for (c,cnt) in bags[color]]
    # print(res)
    return 1+sum(res)

def process_2(rules):
    bags = {}
    rlist = [r.strip().split("contain") for r in rules]
    for r in rlist:
        bag = r[0][:-5].strip()
        contains = [(b,c) for (c,b) in re.findall("(\d) (\w+ \w+)", r[1])]
        # print(bag, contains)
        bags[bag]=contains

    print("two:", rec(bags, "shiny gold")-1)


test_1 = """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

test_2 = """
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""

if __name__ == "__main__":
    # process_1(test_1.strip().split("\n"))
    process_1(read_input())
    # process_2(test_1.strip().split("\n"))
    # process_2(test_2.strip().split("\n"))
    process_2(read_input())



