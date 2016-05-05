# Problem C. Coin Jam
# Google Code Jam 2016
#
# Solution 2 by Zesheng Li
# rexeneo@gmail.com


def bfactor_gen(digit=2, direction=1):
    if direction > 0:
        binary = 2**(digit-1) + 1
        while True:
            yield binary
            binary += 2
    else:
        binary = 2**digit-1
        while True:
            yield binary
            binary -= 2


def coincheck(coin, digit):
    return (coin & (2**(digit-1))) and (coin & 1) and (2**(digit-1) < coin < 2**digit)


def sfactor_gen(s0, i, l):
    if l.__len__() == i: return
    s = s0
    l.append(s)
    if s[-1]=='0':
        if s.__len__() < 20: sfactor_gen(s+'1', i, l)
        if s.__len__() < 20: sfactor_gen(s+'0', i, l)
    else:
        if s.__len__() < 20: sfactor_gen(s+'0', i, l)
    return


def solution(n, j):
    # ga = bfactor_gen(int(n**.5), -1)
    # gb = bfactor_gen(n-int(n**.5), -1)

    l=[]
    sfactor_gen('1', j, l)
    jamcoins=[]
    for fa in l:
        coin = int(fa, 2)*0b11 + 2**(n-1)
        jamcoins.append(bin(coin)[2:])
        output = bin(coin)[2:]
        for base in range(2, 11):
            output += ' '+str(int('11',base))
        print(output)
        j -=1
        if j==0: break


    # sfactor_gen('1', j, l)
    #
    # for fa in ga:
    #     for fb in gb:
    #         coin = fa*fb
    #         if not coincheck(coin, n):
    #             print('bad coin!')
    #             continue
    #         output = bin(coin)[2:]
    #         for base in range(2, 11):
    #             output += ' '+str(int(bin(fa)[2:], 2))
    #             # output += ' ' + str(fa)
    #         print(output+' '+str(fb))
    #         j -=1
    #         if j==0: break
    #     if j==0: break

# solution(16,10)


# solution(32, 50)
if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, J = [int(s) for s in input().split(" ")]
        print("Case #{}:".format(i))
        solution(N, J)
