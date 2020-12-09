# Solution to Day 8

from collections import OrderedDict

def exc(i, p, acc):
    op = i.split()[0]
    arg = int(i.split()[1])
    if op == "acc":
        acc += arg
        p += 1
    if op == "jmp":
        p += arg
    if op == "nop":
        p += 1
    return p, acc

def try_run(instr):
    p, acc = 0, 0
    visited = OrderedDict()
    while True:
        try:
            visited[p] = instr[p].strip()
        except IndexError:
            print("Program completed:", p, acc)
            return True, visited
        (p, acc) = exc(instr[p], p, acc)
        if p in visited:
            print("Loop detected at acc =", acc)
            break
    return False, visited

def process_1(instr):
    (_, visited) = try_run(instr)
    for i in visited:
        instr_tmp = instr.copy()
        op = instr_tmp[i].split()
        if op[0] == "jmp":
            op_new = "nop "+op[1]
            instr_tmp[i] = op_new
        elif op[0] == "nop":
            op_new = "jmp "+op[1]
            instr_tmp[i] = op_new
        else:
            continue
        (res, vnew) = try_run(instr_tmp)
        if res:
            return


def read_input():
    return open("input-8.txt", "r").readlines()

test = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

if __name__ == "__main__":
    # process_1(test.strip().split("\n"))
    process_1(read_input())
    # process_2(test_1.strip().split("\n"))
    # process_2(test_2.strip().split("\n"))
    # process_2(read_input())


