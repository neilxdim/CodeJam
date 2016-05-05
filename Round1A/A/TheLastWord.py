

def solution(S):
    ans = ""
    for c in S:
        if ans=="": ans=c
        elif c>=ans[0]:
            ans = c+ ans
        else:
            ans = ans + c
    print(ans)


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        S = input()
        print("Case #{}: ".format(i), end='')
        solution(S)
