# Solution to Day 3

def read_input():
    inpt = []
    with open("input-3.txt", "r") as f:
        return f.readlines()

def try_slope_1(lines):
    ix = n_trees = 0
    for l in lines:
        l = l.strip()
        # print(l)
        if l[ix] == '#':
            n_trees = n_trees+1
        ix = (ix+3)%len(l)

    return n_trees

def try_slope_2(lines, slope):
    i = ix = n_trees = 0
    (right, down) = slope
    while i < len(lines):
        l = lines[i]
        l = l.strip()
        # print(l)
        if l[ix] == '#':
            n_trees = n_trees+1
        ix = (ix+right)%len(l)
        i = i+down

    return n_trees


if __name__ == "__main__":
    lines = read_input()
    print("one:", try_slope_1(lines))

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    n_trees = 1
    for s in slopes:
        n_trees = n_trees*try_slope_2(lines, s)
    print("two:", n_trees)

