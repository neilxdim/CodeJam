class Kido:
    """
    str self.role:
        ko: LinkO;
        kx: LinkX;
         o: OLoop;
         x: XLoop;
         !: tempflag for identifying new loop.
         ?: dunno yet
     int self.loopid for o, x
     int self.loopmaker, int self.dist2loop for ko, kx
    """
    def __init__(self, id):
        self.id = id
        self.role = '?'  # ? = dunno yet


class Loop:
    def __init__(self):
        self.members = []
        self.maxlen = 0
        self.maxextlen = {}
        self.isx = False


def buildsolution(N, bffof):
    kids = [Kido(i) for i in range(1, N+1)]
    loops = []

    def resolve(kid, crush):
        if kid.role not in '?!':
            print("kid.id={}, kid.role={}, resolve() expects kid with unresolved role.".format(kid.id, kid.role))
            return

        if crush.role[0] == 'k':
            kid.role = crush.role
            kid.loopmaker = crush.loopmaker
            kid.dist2loop = crush.dist2loop + 1
            return
        elif crush.role == 'o' or crush.role == 'x':
            kid.role = 'k' + crush.role
            kid.loopmaker = crush.id
            kid.dist2loop = 1
            return
        else:
            print("kid.id={}, crush.role='{}', resolve() expects crush with a role".format(kid.id, crush.role))
            return

    def resolveloopkids(kid, loopid, isx):
        if kid.role == '?':
            print("kid.id={}, kid.role={}, resolveloopkid() not expecting a '?' mark.".format(kid.id, kid.role))
            return
        if kid.role == 'o' or kid.role == 'x':
            return
        kid.role = 'x' if isx else 'o'
        kid.loopid = loopid
        resolveloopkids(kids[bffof[kid.id-1]-1], loopid, isx)
        return kid.id

    def newloop(kido):
        loop = Loop()
        loops.append(loop)
        loopid = loops.__len__() -1

        def makeloop(_kid):
            if _kid.id not in loop.members:
                loop.members.append(_kid.id)
                loop.maxextlen[_kid.id] = 0
                loop.maxlen += 1
                makeloop(kids[bffof[_kid.id-1]-1])
            return

        makeloop(kido)
        if loop.maxlen == 2:
            loop.isx = True

        return loopid

    def connect(kid, counter=1):    # kid is kido object. kid.role cannot be '?'
        # peek kid's crush before deciding to recursive call
        kid.role = '!'
        crush = kids[bffof[kid.id-1]-1]

        # base cases:
        # if crush role is known, resolve kid's role (this kid can only be ko or kx)
        if crush.role not in '?!':
            resolve(kid, crush)

            # if kid turns out to be kx, update ext link info
            if kid.role == 'kx':
                newextlen = counter + kid.dist2loop -1
                loop = loops[kids[kid.loopmaker-1].loopid]
                diff = newextlen - loop.maxextlen[kid.loopmaker]
                if diff > 0:
                    loop.maxlen += diff
                    loop.maxextlen[kid.loopmaker] += diff

            return 'rk'
        # if crush role is not known but we've touched it before, we have a new loop!
        elif crush.role == '!':
            loopid = newloop(crush)
            resolveloopkids(crush, loopid, loops[loopid].isx)
            return 'r!'

        # otherwise crush.role == '?', call in
        rcode = connect(crush, counter+1)

        # after recursion returned
        if rcode == 'rk' and kid.role == '!':
            resolve(kid, crush)
            return 'rk'
        elif rcode == 'r!':  # back from a new loop, need to check if kid's got a role
            # if kid's already got a loop role, then kid's been taken care of in basecase
            if kid.role == 'o' or kid.role == 'x':
                return 'r!'
            # if rcode is 'r!' but kid.role is unresolved, kid is link end (before loopmaker)!
            else:
                resolve(kid, crush)
                if kid.role == 'kx':
                    newextlen = counter + kid.dist2loop - 1
                    loop = loops[kids[kid.loopmaker - 1].loopid]
                    diff = newextlen - loop.maxextlen[kid.loopmaker]
                    if diff > 0:
                        loop.maxlen += diff
                        loop.maxextlen[kid.loopmaker] += diff
                return 'rk'
        else:
            # else, something went wrong
            print("kid.id={}, kid.role={}, rcode={}, wrong stuff.".format(kid.id, kid.role, rcode))
            return 'badcode'

    for kid in kids:
        if kid.role == '?':
            connect(kid, 1)
    return kids, loops


def solution(N, edge):
    kids, loops = buildsolution(N, edge)
    maxo = 0
    maxx1, maxx2 = 0, 0
    for loop in loops:
        if loop.isx and loop.maxlen > maxx1:
            maxx1 = loop.maxlen
            continue
        elif loop.isx and loop.maxlen > maxx2:
            maxx2 = loop.maxlen
            continue
        if (not loop.isx) and loop.maxlen > maxo:
            maxo = loop.maxlen

    print(maxo if maxo > (maxx1+maxx2) else maxx1+maxx2)

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        N = int(input())
        Q = input()
        bffof = [int(b) for b in Q.split(' ')]
        print("Case #{}: N={}, {}".format(i, N, Q) )
        solution(N, bffof)
