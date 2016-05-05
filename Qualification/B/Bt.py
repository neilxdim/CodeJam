

with open("B-small-attempt0.out") as f, open("b-out2.out") as f2:
    la = []
    lb = []
    for line in f:
        la.append(line.split(' ')[-1])

    for line in f2:
        lb.append(line.split(' ')[-1])

    print(la)
