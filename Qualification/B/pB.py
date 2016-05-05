# Problem B Revenge of the Pancakes

def flip(_cookies):
    _cookies.reverse()
    return ['+' if c == '-' else '-' for c in _cookies]


def solution(s):
    cookies = list(s)
    prev = cookies[0]
    ans = 0
    for i in range(1, cookies.__len__()):
        if cookies[i] != prev:
            cookies[:i] = flip(cookies[:i])
            ans += 1
        prev = cookies[i]

    return ans if prev == '+' else ans+1


if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = input()
        print("Case #{}: {}".format(i, solution(s)))
