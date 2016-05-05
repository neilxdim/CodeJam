# Problem B Revenge of the Pancakes

# def flip(_cookies):
#     _cookies.reverse()
#     return ['+' if c == '-' else '-' for c in _cookies]


def solution(s):
    prev = s[0]
    ans = 0
    for i in range(1, s.__len__()):
        if s[i] != prev:
            ans += 1
        prev = s[i]

    return ans if prev == '+' else ans+1


if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s = input()
        print("Case #{}: {}".format(i, solution(s)))
