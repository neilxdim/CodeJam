import csv

def p(*args): print ' '.join([str(i) for i in args])

with open('t.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        p(row[0], row[1], *[c[:2] for c in row[3:]])

