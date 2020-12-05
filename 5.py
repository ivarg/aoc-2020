# Solution to Day 5


def read_input():
    return open("input-5.txt", "r").readlines()

def decode(n, up, down, code):
    low, high, step = 0, n-1, n/2
    for c in code:
        if c == up:
            low += step
        if c == down:
            high -= step
        step = step/2
    return int(low)

def row(code):
    return decode(128, 'B', 'F', code)

def col(code):
    return decode(8, 'R', 'L', code)

def find_seat(code):
    return row(code[:7]), col(code[7:])

def get_id(row, col):
    return row*8+col

def find_missing(ids):
    min, max = ids[0], ids[-1]
    for i in range(len(ids)-1):
        if ids[i+1]-ids[i] > 1:
            return ids[i]+1

def process(lines):
    ids = [get_id(seat[0], seat[1]) for seat in [find_seat(l) for l in lines]]
    print("one:", max(ids))
    ids = sorted(ids)
    print("two:", find_missing(ids))


def test():
    test = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    process(test)

    test = {"BFFFBBFRRR":(70, 7, 567), "FFFBBBFRRR":(14,7,119), "BBFFBBFRLL":(102,4,820)}
    for k in test.keys():
        (row, col) = find_seat(k)
        print(row, col, get_id(row, col))



if __name__ == "__main__":
    # test()
    process(read_input())

