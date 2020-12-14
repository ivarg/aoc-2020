# Solution to Day 13

def read_input():
    return open("input-13.txt", "r").readlines()

def process1(data):
    t = int(data[0])
    bs = [int(c) for c in data[1].split(",") if c != "x"]
    waits = [b-t%b for b in bs]
    print("one:", min(waits)*bs[waits.index(min(waits))])


def process2(data):
    buses = [(int(c),i) for i,c in enumerate(data[1].split(",")) if c!='x']
    t,m=0,1
    for i,kv in enumerate(buses[:-1]):
        (b,_)=kv
        m*=b
        (id,delta)=buses[i+1]
        while (t+delta)%id != 0:
            t+=m
    print("two:", t)


t1 = """
939
7,13,x,x,59,x,31,19
"""

if __name__ == "__main__":
    # process1(t1.strip().split())
    process1(read_input())
    # process2(t1.strip().split())
    process2(read_input())


