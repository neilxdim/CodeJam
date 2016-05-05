# A

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


if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for case in range(1, t + 1):
        print("Case #{}: {}".format(case, solution(int(input()))))

