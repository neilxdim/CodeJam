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


def sfactor_gen(s0, n, j, l):
    if l.__len__() >= j: return
    s = s0
    if s[-1]=='1' and s.__len__() < (n-3): sfactor_gen(s+'0', n, j, l)
    if s[-1]=='0' and s.__len__() < (n-3):
        sfactor_gen(s+'0', n, j, l)
        sfactor_gen(s+'1', n, j, l)

    if s.__len__() == (n-3): l.append(s+'01')
    return


def solution(n, j):
    # ga = bfactor_gen(int(n**.5), -1)
    # gb = bfactor_gen(n-int(n**.5), -1)

    l=[]
    sfactor_gen('1', n, j, l)
    # jamcoins=[]
    for fa in l:
        coin = bin(int(fa,2) * 0b11)[2:]
        # jamcoins.append(bin(coin)[2:])
        output = coin
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

solution(32,50)

#
# solution(32, 50)
# if __name__ == '__main__':
#     t = int(input())  # read a line with a single integer
#     for i in range(1, t + 1):
#         N, J = [int(s) for s in input().split(" ")]
#         print("Case #{}:".format(i))
#         solution(N, J)
