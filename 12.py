# Solution to Day 12

def read_input():
    return open("input-12.txt", "r").readlines()

def doturtle(ops):
    d = 0
    nops = []
    for (o,n) in ops:
        if o=="F":
            nops += [("ESWN"[d], n)]
        else:
            d = (d+int(n/90))%4 if o=="R" else (d-int(n/90))%4
    return nops

def process_1(data):
    ops = [(l[0],int(l[1:])) for l in data]
    dops = [op for op in ops if op[0] in "NSEW"]
    tops = [op for op in ops if op[0] in "FRL"]
    dops += doturtle(tops)

    n = sum([n for (o,n) in dops if o=="N"])
    s = sum([n for (o,n) in dops if o=="S"])
    e = sum([n for (o,n) in dops if o=="E"])
    w = sum([n for (o,n) in dops if o=="W"])
    print("one:",abs(n-s)+abs(e-w))


def movewp(x,y,o,n):
    if o=="N":
        return (x,y+n)
    elif o=="S":
        return (x,y-n)
    elif o=="E":
        return (x+n,y)
    elif o=="W":
        return (x-n,y)

def rotatewp(x,y,o,n):
    steps = int((n/90)%4)
    if steps == 2:
        return (-x,-y)
    if steps == 1:
        return (y,-x) if o=="R" else (-y,x)
    elif steps == 3:
        return (-y,x) if o=="R" else (y,-x)

def process_2(data):
    x,y = 10,1
    ship = (0,0)
    ops = [(l[0],int(l[1:])) for l in data]
    for (o,n) in ops:
        if o=="F":
            ship = ship[0]+n*x, ship[1]+n*y
        elif o in "NESW":
            (x,y) = movewp(x,y,o,n)
        else:
            (x,y) = rotatewp(x,y,o,n)
    print("two:",abs(ship[0])+abs(ship[1]))


t = """
F10
N3
F7
R90
F11
"""

if __name__ == "__main__":
    # process_1(t.strip().split())
    process_1(read_input())
    # process_2(t.strip().split())
    process_2(read_input())

