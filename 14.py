# Solution to Day 14

def read_input():
    return open("input-14.txt", "r").readlines()

def mask(msk, val):
    bval = "{0:b}".format(val).zfill(36)
    res = "".join([b if m=="X" else m for (b,m) in zip(bval, msk)])
    return int(res,2)

def process1(data):
    msk = []
    mem = {}
    for line in data:
        instr = line.strip().split()
        if instr[0] == "mask":
            msk = instr[2]
        else:
            addr = int(instr[0].split("[")[1][:-1])
            bval = "{0:b}".format(int(instr[2])).zfill(36)
            res = "".join([b if m=="X" else m for (b,m) in zip(bval, msk)])
            mem[addr]=int(res,2)

    print("one:", sum(mem.values()))


def explode(msk):
    for i,c in enumerate(msk):
        if c=="X":
            m0 = msk[:i]+"0"+msk[i+1:]
            m1 = msk[:i]+"1"+msk[i+1:]
            return explode(m0) + explode(m1)
    return [msk]

def process2(data):
    writes = {}
    for line in data:
        instr = line.strip().split()
        if instr[0] == "mask":
            msk = instr[2]
        else:
            addr = int(instr[0].split("[")[1][:-1])
            addr = "{0:b}".format(addr).zfill(36)
            val = int(instr[2])
            maddr = "".join([a if m=="0" else m for (a,m) in zip(addr, msk)])
            addrs = explode(maddr)
            for a in addrs:
                writes[a]=val
    print("two:",sum(writes.values()))


t1 = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""

t2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""

if __name__ == "__main__":
    # process1(t1.strip().split("\n"))
    process1(read_input())
    # process2(t2.strip().split("\n"))
    process2(read_input())


