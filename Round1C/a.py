import sys, traceback
sys.setrecursionlimit(5000)


def solution(N):



if __name__ == '__main__':

    t = int(input())
    for i in range(1, t + 1):
        N = int(input())
        a = input().split(' ')
        print("Case #{}: ".format(i), end='')
        print(solution(N))
        # try:
        #     print(solution(N, bffof))
        # except Exception as ex:
        #     # print(type(ex).__name__, ex.args)
        #     traceback.print_exc()


