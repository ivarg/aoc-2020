# Solution for Day 1

def read_input():
    inpt = []
    with open("input-1.txt", "r") as f:
        lines = f.readlines()
        inpt = [int(l) for l in lines]
        return inpt

def findtwo(ls):
    for a in ls:
        for b in reversed(ls):
            if a + b == 2020:
                return (a,b)

def findthree(ls):
    for i, a in list(enumerate(ls)):
        for b in ls[i+1:]:
            for c in reversed(ls[i+1:]):
                if a+b+c == 2020:
                    return (a,b,c)


if __name__ == "__main__":
    i = read_input()
    (a, b) = findtwo(sorted(i))
    print("two:", a*b)
    (a,b,c) = findthree(sorted(i))
    print("three:", a*b*c)
