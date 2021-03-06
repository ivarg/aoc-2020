# Solution to Day 11

def read_input():
    return open("input-11.txt", "r").readlines()

def totext(seating):
    lines = []
    for j in range(DIM):
        l = ""
        for i in range(DIM):
            if (i,j) in seating:
                l += "L" if seating[(i,j)] == 0 else "#"
            else:
                l += "."
        lines.append(l)
    return lines

def fromtext(data):
    seating = {}
    for j,l in enumerate(data):
        for i,v in enumerate(l.strip()):
            if v == ".":
                continue
            if v == "L":
                iv = 0
            else:
                iv = 1
            seating[(i,j)] = iv
    return seating


def nbsum_2(seating, i, j):
    def checkdir(dfun):
        for x in range(1,DIM):
            (i,j) = dfun(x)
            if (i,j) in seating:
                return seating[(i,j)]
        return 0

    sum = 0
    sum += checkdir(lambda x: (i,j-x)) # up
    sum += checkdir(lambda x: (i,j+x)) # down
    sum += checkdir(lambda x: (i-x,j)) # left
    sum += checkdir(lambda x: (i+x,j)) # right
    sum += checkdir(lambda x: (i-x,j-x)) # up/left
    sum += checkdir(lambda x: (i+x,j-x)) # up/right
    sum += checkdir(lambda x: (i+x,j+x)) # down/right
    sum += checkdir(lambda x: (i-x,j+x)) # down/left

    return sum

def nbsum_1(seating, i, j):
    above = [(i-1,j-1),(i,j-1),(i+1,j-1)]
    sides = [(i-1,j),(i+1,j)]
    below = [(i-1,j+1),(i,j+1),(i+1,j+1)]
    nb = above+sides+below
    return sum([seating[(i,j)] for (i,j) in nb if (i,j) in seating])


def iterate_1(seating):
    newseating = seating.copy()
    for (i,j), v in seating.items():
        if v == 1 and nbsum_1(seating, i, j) >= 4:
            newseating[(i,j)] = 0
        if v == 0 and nbsum_1(seating, i, j) == 0:
            newseating[(i,j)] = 1
    return newseating


def iterate_2(seating):
    newseating = seating.copy()
    for (i,j), v in seating.items():
        if v == 1 and nbsum_2(seating, i, j) >= 5:
            newseating[(i,j)] = 0
        if v == 0 and nbsum_2(seating, i, j) == 0:
            newseating[(i,j)] = 1
    return newseating


def process(data, iterate_fn):
    st = fromtext(data)

    iter, same = 0, False
    while not same:
        iter += 1
        nst = iterate_fn(st)
        # for l in totext(nst):
            # print(l)
        # print()
        same = 0 == len({k:st[k] for k in st if k in nst and st[k] != nst[k]})
        st = nst

    # for l in totext(nst):
        # print(l)
    print("seats:", sum([st[k] for k in st]))

t1 = """
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

def run():
    global DIM

    DIM=10
    # process(t1.strip().split(), iterate_2)

    DIM=97
    print("one")
    process(read_input(), iterate_1)
    print("two")
    process(read_input(), iterate_2)


run()

