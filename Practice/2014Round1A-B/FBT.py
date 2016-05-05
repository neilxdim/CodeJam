import sys
sys.setrecursionlimit(5000)


def countn(node, parent, elist):
    max1 = max2 = 0
    for child in elist[node]:
        if child == parent: continue
        n = countn(child, node, elist)
        if n > max2:
            if n > max1:
                max2 = max1
                max1 = n
            else:
                max2 = n

    return max1+max2+1 if max2 != 0 else 1


def solution(N, a):
    elist = [set() for _ in range(N)]
    for edge in a:
        elist[edge[0]].add(edge[1])
        elist[edge[1]].add(edge[0])

    maxn = 0
    for root in range(N):
        maxn = max(maxn, countn(root, -1, elist))
    return N-maxn


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        N = int(input())
        a=[]
        for line in range(N-1):
            a.append([int(i)-1 for i in input().split(' ')])
        print("Case #{}: ".format(i), end='')
        print(solution(N, a))
