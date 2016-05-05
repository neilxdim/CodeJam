# Problem D. Fractiles
# Google Code Jam 2016
# https://code.google.com/codejam/contest/6254486/dashboard#s=p3
#
# revised solution by Zesheng Li
# rexeneo@gmail.com


def solution(K, C, S):
    if C*S < K:
        print('IMPOSSIBLE')
        return

    ans = []
    for i in range(1, K+1, C):
        pos = 1
        for ii in range(C):
            pos = (pos-1)*K + min(i + ii, K)
        ans.append(pos)

    print(' '.join([str(i) for i in ans]))
    return

if __name__ == '__main__':
    import traceback

    t = int(input())
    for i in range(1, t + 1):
        K, C, S = [int(s) for s in input().split(" ")]
        print("Case #{}: ".format(i), end='')
        # try:
        solution(K, C, S)
        # except Exception:
        #     traceback.print_exc()

