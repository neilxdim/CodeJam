
class Kid:
    def __init__(self, id=None, crush=None):
        self.id = id
        self.crush = crush
        self.tag = None
        self.lowlink = None
        self.loopid = None
        self.rootkid = None
        self.dist2root = None
        self.onstack = False


class Loop:
    def __init__(self, id=None):
        self.id = id
        self.members = []
        self.extdict = {}


def solution(N, bffof):
    kidlist = [Kid(id=i+1) for i in range(N)]
    looplist = []
    for i, crush_id in enumerate(bffof):
        kidlist[i].crush = kidlist[crush_id-1]

    tagnum = [1]
    stack = []

    def connect(kid):
        # nonlocal tagnum
        kid.tag = kid.lowlink = tagnum[0]
        tagnum[0] += 1
        stack.append(kid)
        kid.onstack = True

        if kid.crush.tag is None:
            connect(kid.crush)
            kid.lowlink = min(kid.lowlink, kid.crush.lowlink)
        elif kid.crush.onstack:  # if crush is visited but still onstack, it's still in current scc
            kid.lowlink = min(kid.lowlink, kid.crush.lowlink)

        if kid.lowlink == kid.tag:
            if stack[-1] is not kid:
                newloop = Loop(looplist.__len__()+1)
                looplist.append(newloop)
                while True:
                    popped = stack.pop()
                    popped.onstack = False
                    newloop.members.append(popped)
                    popped.loopid = newloop.id
                    popped.rootkid = popped
                    popped.dist2root = 0
                    if popped is kid:
                        break
            else:  # kid being stack top meaning kid is not in loop
                popped = stack.pop()
                popped.onstack = False
                popped.rootkid = popped.crush.rootkid
                popped.dist2root = popped.crush.dist2root + 1
                if stack.__len__() == 0:  # kid is so far the furtherest kid
                    extdict = looplist[popped.rootkid.loopid - 1].extdict
                    if popped.rootkid not in extdict or popped.dist2root > extdict[popped.rootkid]:
                        extdict[popped.rootkid] = popped.dist2root

    for kid in kidlist:
        if kid.tag is None:
            connect(kid)

    # get longest loop
    maxlooplen = 0
    sumcoupleext = 0
    for loop in looplist:
        maxlooplen = max(loop.members.__len__(), maxlooplen)
        if loop.members.__len__() == 2:
            sumcoupleext += sum(loop.extdict.values()) + 2
    return sumcoupleext if sumcoupleext > maxlooplen else maxlooplen


if __name__ == '__main__':
    import sys, traceback
    sys.setrecursionlimit(5000)

    t = int(input())
    for i in range(1, t + 1):
        N = int(input())
        bffof = [int(b) for b in input().split(' ')]
        print("Case #{}: ".format(i), end='')
        try:
            print(solution(N, bffof))
        except Exception as ex:
            # print(type(ex).__name__, ex.args)
            traceback.print_exc()
