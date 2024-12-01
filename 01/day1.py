
a, b = [], []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)

a.sort()
b.sort()

print(sum(abs(a[i]-b[i]) for i in range(len(a))))

from collections import Counter

occ = Counter(b)
sim_score = sum(occ[num] * num for num in a)
print(sim_score)
