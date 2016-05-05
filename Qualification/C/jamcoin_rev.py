# Problem C. Coin Jam
# Google Code Jam 2016
#
# Solution 2 by Zesheng Li
# rexeneo@gmail.com

# 110.... + 011
def coingen(N, sofar='110'):
    if len(sofar) == N-3:
        yield sofar+'011'
    else:
        if len(sofar) <= N-5:
            yield from coingen(N, sofar+'11')
        yield from coingen(N, sofar+'0')

def solution(N, J):
    div = [str(int('11', b)) for b in range(2, 11)]

    for i, coin in enumerate(coingen(N)):
        print("{} {}".format(coin, ' '.join(div)))
        if i == J-1: break


if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, J = [int(s) for s in input().split(" ")]
        print("Case #{}:".format(i))
        solution(N, J)
