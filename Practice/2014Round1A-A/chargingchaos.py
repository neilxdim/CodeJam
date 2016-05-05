# import copy


def solution(N, L, a, b):
    # a = [[int(d) for d in i] for i in a]
    # b = [[int(d) for d in i] for i in b]
    # bset = {''.join(str(i)) for i in b}

    bset = set(b)
    minflip = L+1
    for ai in a:
        fail = False
        acopy = a[:]
        counter = 0
        for d in range(L):
            if ai[d] != b[0][d]:
                counter += 1
                for i in range(N):
                    outlet = acopy[i]
                    acopy[i] = outlet[:d] + ('1' if outlet[d] == '0' else '0') + outlet[d+1:]
        for outlet in acopy:
            if outlet not in bset:
                fail = True
                break
        if fail: continue
        minflip = min(minflip, counter)
    return minflip


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        N, L = input().split(' ')
        N, L = int(N), int(L)
        als = input().split(' ')
        bls = input().split(' ')
        print("Case #{}: ".format(i), end='')
        ans = solution(N, L, als, bls)
        print('{}'.format(ans if ans != L+1 else 'NOT POSSIBLE'))
