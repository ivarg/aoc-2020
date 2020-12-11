# Solution to Day 11

from collections import OrderedDict

global DIM

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
    global DIM

    sum = 0
    for x in range(1,DIM): # up
        k = (i,j-x)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # down
        k = (i,j+x)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # left
        k = (i-x,j)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # right
        k = (i+x,j)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # up/left
        k = (i-x,j-x)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # up/right
        k = (i+x,j-x)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # down/right
        k = (i+x,j+x)
        if k in seating:
            sum += seating[k]
            break
    for x in range(1,DIM): # down/left
        k = (i-x,j+x)
        if k in seating:
            sum += seating[k]
            break
    return sum

def nbsum_1(seating, i, j):
    above = [(i-1,j-1),(i,j-1),(i+1,j-1)]
    same = [(i-1,j),(i+1,j)]
    below = [(i-1,j+1),(i,j+1),(i+1,j+1)]
    nb = above+same+below
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


def process_1(data):
    st = fromtext(data)

    iter, same = 0, False
    while not same:
        iter += 1
        nst = iterate_2(st)
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

if __name__ == "__main__":
    DIM=10
    # process_1(t1.strip().split())

    DIM=97
    process_1(read_input())
    # process_2([int(x) for x in t2.strip().split()])
    # process_2([int(x) for x in read_input()])

