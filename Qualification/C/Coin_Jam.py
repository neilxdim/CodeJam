# Problem C. Coin Jam
# Google Code Jam 2016


# Fermat primality test. Might have pseudoprime but we only need composites
def fermat_prime(num):
    if num == 2:
        return True
    if not num & 1:  # even num can't be prime
        return False
    return pow(2, num-1, num) == 1


def prime_gen(seed=1):
    if seed == 1 or seed == 0: yield 2
    if seed & 1:   # is odd and gt 1
        seed += 2
    else:
        seed += 1
    while True:
        if fermat_prime(seed):
            yield seed
        seed += 2


def find_divisor(num):
    bound = int(num**.5)
    for d in prime_gen():
        if d > bound:
            print(str(num)+" broke some stuff")
            return
        if (num % d) == 0:
            return d


def solution(n, j):
    for coin_d in range(2**(n-1)+1, 2**n, 2):
        if j == 0: break
        coin = bin(coin_d)[2:]  # represented as string '11101'
        for base in range(2, 11):
            if fermat_prime(int(coin, base)):
                break   # maybe a fake coin
        else:  # must be genuine coin (composite)
            coinmeta = [coin]
            for base in range(2, 11):
                coinmeta.append(find_divisor(int(coin, base)))
            j -= 1
            print(' '.join(str(e) for e in coinmeta))


if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, J = [int(s) for s in input().split(" ")]
        print("Case #{}:".format(i))
        solution(N, J)
