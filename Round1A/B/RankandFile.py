

def solution(N, grid):
    it = [int(i) for row in grid for i in row]
    dict = {}
    for i in it:
        if dict.get(i) is None:
            dict[i] = i
        else:
            dict[i] ^= i
    return sorted([i for i in dict.keys() if dict[i]])


if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        N = int(input())
        grid = []
        for row in range(2*N-1):
            grid.append(input().split(' '))
        print("Case #{}: ".format(i), end='')
        try:
            for i in solution(N, grid):
                print(i, end=' ')
            print()
        except Exception as ex:
            print(ex)
