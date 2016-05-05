def igen(start=0):
    while True:
        yield start
        start += 1


def solution(N):
    if N == 0: return "INSOMNIA"
    s = set({})
    for i in igen(1):
        sn = str(i*N)
        for d in sn: s.add(d)
        if s.__len__() == 10: return sn

with open("c.txt") as f:
    for line in f:
        print(solution(int(line)))

