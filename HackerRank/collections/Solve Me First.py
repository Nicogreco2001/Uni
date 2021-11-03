from collections import defaultdict
n, m = input().split()
n, m = int(n), int(m)
A = []
B = []
for a in range(n):
    A.append(input())
for b in range(m):
    B.append(input())

for b in B:
    sol = defaultdict(list)
    count = 0
    while count < len(A):
        if b == A[count]:
            sol[b].append(count)

for i in sol:
    print(i)


