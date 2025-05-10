import sys

input = sys.stdin.readline

k = int(input())
lst = []
sum = 0

for i in range(k):
    v = int(input())
    if v==0:
        if not lst:
            continue
        else:
            lst.pop()
    else:
        lst.append(v)

for j in lst:
    sum += j

print(sum)


