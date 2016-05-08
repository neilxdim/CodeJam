import sys
sys.setrecursionlimit(5000)

def rp(s, i, c):
    return s[:i] + str(c) + s[i+1:]


def solution(C, J):
    diff = 9999999999999999999
    cj = ['', '']
    L = len(C)

    def check(c, j, big=-1, i=0):
        nonlocal diff
        if i == L:
            if cj == ['', ''] or abs(int(c) - int(j)) < diff:
                cj[0], cj[1] = c, j
                diff = abs(int(c) - int(j))
                return
            elif diff == abs(int(c) - int(j)):
                if c < cj[0] or (c == cj[0] and j < cj[1]):
                    cj[0], cj[1] = c, j
                    diff = abs(int(c) - int(j))
                    return
            return

        if c[i] != '?' and j[i] != '?':
            if big == -1 and c[i] > j[i]:
                big = 0
            elif big == -1 and c[i] < j[i]:
                big = 1
            check(c, j, big, i+1)
        elif c[i] == j[i] == '?':
            if big == -1:
                if i+1 != L and c[i+1] == j[i+1] == '?':
                    check(rp(c,i,0), rp(j,i,0), big, i + 1)
                else:
                    check(rp(c, i, 0), rp(j, i, 0), big, i + 1)
                    check(rp(c, i, 1), rp(j, i, 0), 0, i + 1)
                    check(rp(c, i, 0), rp(j, i, 1), 1, i + 1)
                    check(rp(c, i, 1), rp(j, i, 1), big, i + 1)
            elif big == 0:
                check(rp(c, i, 0), rp(j, i, 9), big, i + 1)
            elif big == 1:
                check(rp(c, i, 9), rp(j, i, 0), big, i + 1)
        else:
            if big == -1:
                if c[i] == '?':
                    check(rp(c, i, j[i]), j, big, i + 1)
                    if j[i] != '9':
                        check(rp(c, i, int(j[i])+1), j, 0, i + 1)
                    if j[i] != '0':
                        check(rp(c, i, int(j[i])-1), j, 1, i + 1)
                else:
                    check(c, rp(j, i, c[i]), big, i + 1)
                    if c[i] != '9':
                        check(c, rp(j, i, int(c[i])+1), 1, i + 1)
                    if c[i] != '0':
                        check(c, rp(j, i, int(c[i])-1), 0, i + 1)
            elif big == 0:
                if c[i] =='?':
                    c = rp(c,i,0)
                else:
                    j = rp(j,i,9)
                check(c, j, big, i + 1)
            elif big == 1:
                if c[i] =='?':
                    c = rp(c,i,9)
                else:
                    j = rp(j,i,0)
                check(c, j, big, i + 1)

    check(C, J)
    return cj

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        C, J = input().split(' ')
        print("Case #{}: ".format(i), end='')
        print(*solution(C, J))
