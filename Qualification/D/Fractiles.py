# Problem D. Fractiles
# Google Code Jam 2016
# https://code.google.com/codejam/contest/6254486/dashboard#s=p3
#
# solution by Zesheng Li
# rexeneo@gmail.com


def myidx(k):
    return [[i, min(i + 1, k)] for i in range(1, k + 1, 2)]


def tile_position(k, c, i, j):
    pos = 0
    while c > 1:
        c -= 1
        pos += (i-1)*(k**c)
    return pos+j


def crit_tile(K, C):
    if C == 1:
        return [i+1 for i in range(K)]
    ans = []
    for i, j in myidx(K):
        # ans.append((i-1)*(K**(C-1))+(j**(C-1)))
        ans.append( tile_position(K, C, i, j) )
    return ans


def solution(K, C, S):
    checktile = crit_tile(K, C)
    if checktile.__len__() > S:
        print('IMPOSSIBLE')
        return
    print(' '.join([str(i) for i in checktile]))


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        K, C, S = [int(s) for s in input().split(" ")]
        print("Case #{}: ".format(i), end='')
        solution(K, C, S)


