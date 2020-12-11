# Solution to Day 10

from collections import Counter

# First puzzle

def read_input():
    return open("input-10.txt", "r").readlines()

def process_1(data):
    d = [0] + sorted(data)
    d = Counter([(b-a) for (a,b) in zip(d, d[1:])])
    print(d)
    print("one:", d[1] * (d[3]+1))
    return d

# Second puzzle
# For each group of ones, calculate the number of possible
# permutations

def merge(a,b):
    return [i+j for i in a for j in b]

def rec(ones):
    res =[]

    if len(ones) == 1:
        return [[1]]
    if len(ones) == 2:
        return [ones, [2]]
    if len(ones) == 3:
        res = [(3,)]

    for i in range(1, len(ones)):
        a = rec(ones[:i])
        a = [tuple(l) for l in a]

        b = rec(ones[i:])
        b = [tuple(l) for l in b]

        res += merge(a,b)
        res = list(set(res))
    return res

def process_2(data):
    d = [0] + sorted(data)
    d = [(b-a) for (a,b) in zip(d, d[1:])]
    i, res = 0,1
    while i<len(d):
        if d[i]==1 and d[i+1]==1 :
            a,b=i,i+2
            while b<len(d) and d[b]==1:
                b+=1
            res *= len(rec(d[a:b]))
            i=b-1
        i+=1
    print("two:", res)




    # print(rec(d))
    # print(len(rec(d))+1)
    # d = Counter([1 for (a,b,c) in zip(d, d[1:], d[2:]) if c-a==2])
    # print(2**d[1])

    # d = [(b-a) for (a,b) in zip(d, d[1:])]
    # for i,v in enumerate(d):
        # pass


t1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

t2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

if __name__ == "__main__":
    # process_1([int(x) for x in t1.strip().split()])
    # process_1([int(x) for x in read_input()])
    # process_2([int(x) for x in t2.strip().split()])
    process_2([int(x) for x in read_input()])
    # process_2([int(x) for x in test.strip().split("\n")], 5)
    # process_2([int(x) for x in read_input()], 25)

