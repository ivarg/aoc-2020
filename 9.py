# Solution to Day 9

def read_input():
    return open("input-9.txt", "r").readlines()

def isvalid(dt, x):
    return x in [dt[i]+dt[j] for i in range(len(dt)) for j in range(i+1, len(dt))]


def process_1(data, p):
    for i in range(len(data)-p):
        if not isvalid(data[i:i+p], data[i+p]):
            print("one:", data[i+p])
            return data[i+p]

def process_2(data, p):
    x = process_1(data, p)

    for i in range(len(data)-p):
        for j in range(i+1, len(data)):
            if sum(data[i:j]) == x:
                two = min(data[i:j]) + max(data[i:j])
                print("two:", two)
                return


test = """
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""

if __name__ == "__main__":
    # process_1([int(x) for x in test.strip().split("\n")], 5)
    # process_1([int(x) for x in read_input()])
    # process_2([int(x) for x in test.strip().split("\n")], 5)
    process_2([int(x) for x in read_input()], 25)

