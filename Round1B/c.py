import sys
sys.setrecursionlimit(5000)


def solution(N, t):
    a={}
    b={}
    ans = 0
    for title in t:
        if title[0] not in a:
            a[title[0]] = 1
        else:
            a[title[0]] +=1
        if title[1] not in b:
            b[title[1]] =1
        else:
            b[title[1]] +=1
    while True:
        ok = True
        for pair in t:
            p, q = pair
            if a[p] > 1 and b[q] > 1:
                ans +=1
                a[p] -=1
                b[q] -=1
                t.remove(pair)
                ok = False
        if ok: break
    return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        N = int(input())
        t=[]
        for line in range(N):
            t.append(input().split(' '))
        print("Case #{}: ".format(i), end='')
        print(solution(N, t))
