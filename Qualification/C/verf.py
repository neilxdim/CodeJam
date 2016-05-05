with open('verif.txt') as f:
    for l in f:
        ll=l.split()
        vl=[ll[0]]
        for i, d in enumerate(ll[1:]):
            conv = int(ll[0], i+2)
            vl.append(str(conv%int(d)))
        print(' '.join(vl))

