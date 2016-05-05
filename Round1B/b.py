import sys
sys.setrecursionlimit(5000)


def rp(s, i, w):
    w = str(w)
    return s[:i] + w + s[i+1:]

def solution(C, J):
    L = len(C)
    stack = [(C,J,-1)]
    cand = [99999999999999999999,[]]
    while len(stack) != 0:
        c, j, big = stack.pop()
        # p = (c,j)
        ok = True
        for i in range(L):
            if c[i]=='?' and j[i]=='?':
                if big == -1:
                    if i <(L-1) and c[i+1]==j[i+1]=='?':
                        stack += [(rp(c, i, 0), rp(j, i, 0), -1)]
                    else:
                        stack += [(rp(c, i, 0), rp(j,i, 0), -1),
                                  (rp(c, i, 1), rp(j,i, 0), 0),
                                  (rp(c, i, 0), rp(j,i, 1), 1),
                                  (rp(c, i, 1), rp(j,i, 1), -1)]
                    ok = False
                    break
                else:
                    if big==0:
                        stack += [(rp(c, i, 0), rp(j, i, 9), big)]
                    else:
                        stack += [(rp(c, i, 9), rp(j, i, 0), big)]
                    ok = False
                    break
            if c[i]=='?' and big ==0:
                stack += [(rp(c, i, 0), j, big)]
                ok = False
                break
            if c[i]=='?' and big ==1:
                stack += [(rp(c, i, 9), j, big)]
                ok = False
                break
            if j[i] == '?' and big == 1:
                stack += [(c, rp(j,i,0), big)]
                ok = False
                break
            if j[i] == '?' and big ==0:
                stack += [(c, rp(j, i, 9), big)]
                ok = False
                break
            if c[i] =='?' and big ==-1:
                stack += [( rp(c, i, j[i]), j, big)]
                if j[i] !='9':
                    stack += [(rp(c, i, int(j[i])+1), j, 0)]
                if j[i] !='0':
                    stack += [(rp(c, i, int(j[i])-1), j, 1)]
                ok = False
                break
            if j[i] =='?' and big ==-1:
                stack += [( c, rp(j, i, c[i]), big)]
                if c[i] !='9':
                    stack += [(c, rp(j, i, int(c[i])+1), 1)]
                if c[i] !='0':
                    stack += [(c, rp(j, i, int(c[i])-1), 0)]
                ok = False
                break
            if big==-1 and c[i]>j[i]:
                big=0
            elif big==-1 and c[i]<j[i]:
                big=1

        if not ok:
            continue
        ic, ij = int(c), int(j)
        diff = abs(ic-ij)

        if diff==cand[0]:
            cand[1].append([ic,ij])
        elif diff < cand[0]:
            cand[0] = diff
            cand[1] = [[ic, ij]]

        ans = []
        if len(cand[1]) !=1:
            minc = 99999999999999999999
            for p in cand[1]:
                if p[0]==minc:
                    ans.append(p)
                elif p[0]<minc:
                    ans = [p]
                    minc = p[0]
            if len(ans) >1:
                an = ans[:]
                ans = []
                minj = 99999999999999999999
                for p in an:
                    if p[1]==minj:
                        ans.append(p)
                    elif p[1]<minj:
                        ans = [p]
                        minj=p[1]
        else:
            ans = cand[1][:]

    c, j = str(ans[0][0]), str(ans[0][1])
    cf = L - len(c)
    jf = L - len(j)
    for _ in range(cf):
        c='0'+c
    for _ in range(jf):
        j='0'+j
    return c,j

# print(*solution('0?????????????????', '?????????????????9'))

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        C, J = input().split(' ')
        print("Case #{}: ".format(i), end='')
        print(*solution(C, J))
