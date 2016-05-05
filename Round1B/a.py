import sys
sys.setrecursionlimit(5000)


def solution(S):
    a = {chr(i+65):0 for i in range(26)}
    for l in S:
        a[l] +=1

    ans = ''
    while a['Z'] != 0:
        ans += '0'
        a['Z'] -=1
        a['E'] -=1
        a['R'] -=1
        a['O'] -=1
    while a['W'] !=0:
        ans += '2'
        a['T'] -=1
        a['W'] -=1
        a['O'] -=1
    while a['U'] !=0:
        ans += '4'
        a['F'] -=1
        a['O'] -=1
        a['U'] -=1
        a['R'] -=1
    while a['X'] !=0:
        ans += '6'
        a['S'] -=1
        a['I'] -=1
        a['X'] -=1
    while a['G'] !=0:
        ans += '8'
        a['E'] -=1
        a['I'] -=1
        a['G'] -=1
        a['H'] -=1
        a['T'] -=1
# phase 2
    while a['O'] !=0:
        ans += '1'
        a['O'] -=1
        a['N'] -=1
        a['E'] -=1
    while a['H'] !=0:
        ans += '3'
        a['T'] -=1
        a['H'] -=1
        a['R'] -=1
        a['E'] -=2
    while a['F'] !=0:
        ans += '5'
        a['F'] -=1
        a['I'] -=1
        a['V'] -=1
        a['E'] -=1
    while a['S'] !=0:
        ans += '7'
        a['S'] -=1
        a['E'] -=2
        a['V'] -=1
        a['N'] -=1
    while a['N'] !=0:
        ans += '9'
        a['N'] -=2

    return ''.join(sorted(ans))

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        S = input()
        print("Case #{}: ".format(i), end='')
        print(solution(S))
